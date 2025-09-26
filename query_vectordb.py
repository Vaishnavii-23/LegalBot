# query_vectordb.py

import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

persist_directory_name = os.getenv("PERSIST_DIRECTORY_NAME")

base_path = os.path.dirname(os.path.abspath(__file__))
persist_directory_path = os.path.join(base_path, persist_directory_name)


query = "What is the IPC section for Theft?"

db = Chroma(
    collection_name="ipc_collection",
    persist_directory=persist_directory_path,
    embedding_function=HuggingFaceEmbeddings()
)

docs = db.similarity_search(query, k=3)

# print(docs[0].page_content)
# print(docs)



result = []

for doc in docs:
    result.append({
        "section": doc.metadata.get("section"),
        "section_title": doc.metadata.get("section_title"),
        "chapter": doc.metadata.get("chapter"),
        "chapter_title": doc.metadata.get("chapter_title"),
        "content": doc.page_content
    })

print(result)
