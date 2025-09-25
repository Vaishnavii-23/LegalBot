# ipc_sections_search_tool.py

import os

from dotenv import load_dotenv
from crewai.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


@tool("IPC Sections Search Tool")
def search_ipc_sections(query: str) -> list[dict]:
    """
    Search IPC vector database for sections relevant to the input query.

    Args:
        query (str): User query in natural language.

    Returns:
        list[dict]: List of matching IPC sections with metadata and content.
    """
    # Load environment variables
    load_dotenv()

    # Resolve vector DB path
    persist_dir = os.getenv("PERSIST_DIRECTORY_PATH")
    if not persist_dir:
        raise EnvironmentError("❌ 'PERSIST_DIRECTORY_PATH' is not set in .env")

    persist_dir_path = os.getenv("PERSIST_DIRECTORY_PATH")
    collection_name = os.getenv("IPC_COLLECTION_NAME")

    embedding_function = HuggingFaceEmbeddings()

    # Load vectorstore
    vector_db = Chroma(
        collection_name=collection_name,
        persist_directory=persist_dir_path,
        embedding_function=embedding_function
    )

    top_k = 3 # can be passed as an argument for flexibility

    # Perform similarity search
    docs = vector_db.similarity_search(query, k=top_k)

    # Format results
    return [
        {
            "section": doc.metadata.get("section"),
            "section_title": doc.metadata.get("section_title"),
            "chapter": doc.metadata.get("chapter"),
            "chapter_title": doc.metadata.get("chapter_title"),
            "content": doc.page_content
        }
        for doc in docs
    ]


# Example usage of the IPC Section Search Tool - uncomment for testing the tool functionality
# query = "What is the IPC section for Theft?"
# results = search_ipc_sections.func(query)
# for r in results:
#     print(r)

# NOTE: Retrieval is a bit slower. Can be improved by caching the vectordb and using GPU for embedding.
