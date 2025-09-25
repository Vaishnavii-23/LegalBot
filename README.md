# LegalBot – AI-Powered Multi-Agent Legal Assistant

---

## **Project Overview**
LegalBot is a **multi-agent AI system** designed to **make legal information accessible, understandable, and actionable** for the general public. By leveraging **CrewAI**, LegalBot can coordinate multiple AI agents to handle tasks like understanding legal queries, researching relevant laws, drafting documents, and providing context-aware responses.  

> ⚠️ **Disclaimer:** LegalBot provides **general informational guidance only**. It is **not a substitute for professional legal advice**. Users seeking personalized legal counsel should consult a licensed lawyer.

---

## **Team Members**
- Vaishnavi Ghuge  
- Mayuri Patil  
- Aditya Suryawanshi  
- Pankaj Bhise  

---

## **Key Features**
- **Multi-Agent Coordination**: Uses CrewAI to manage AI agents specialized in classification, legal research, and document drafting.  
- **Query Understanding**: Classifies user queries into procedural, contractual, or general legal categories.  
- **Legal Research & Reference**: Retrieves relevant acts, sections, and precedent cases from curated datasets and public sources.  
- **Document Drafting**: Automatically drafts FIRs, agreements, notices, and other legal documents.  
- **Bilingual Support**: Provides responses in **English and Hindi**.  
- **Interactive Frontend**: Streamlit interface for user-friendly interaction with LegalBot.  
- **Safety & Disclaimers**: Clear guidance to consult licensed lawyers for personalized advice.  

---

## **Technology Stack**
- **Backend**: Python + FastAPI / Flask  
- **Frontend**: Streamlit  
- **Multi-Agent Framework**: CrewAI  
- **NLP / LLM**: Grok (Meta) – generative AI for legal reasoning and drafting
- **Document Parsing**: pdfminer.six, Tesseract OCR, unstructured  
- **Vector Database**: Chroma / FAISS / Pinecone  
- **Data Format**: JSON / CSV for easy ingestion  

---

## **How It Works**
1. **User Query / Document Upload**: Users ask a question or upload a legal document.  
2. **Intent Classification**: Determines if the query is procedural, contractual, or general.  
3. **Multi-Agent Processing**:
   - **Research Agent** → searches dataset/public sources for laws and sections  
   - **Drafting Agent** → generates relevant legal document drafts  
   - **Response Agent** → creates clear, step-by-step answers  
4. **Output**: Displays responses via Streamlit with references, required documents, fees, and timelines.  

---

## **Installation & Usage**
1. Clone the repository:
```bash
git clone https://github.com/yourusername/LegalBot.git
cd LegalBot
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3.Run the backend server:
```bash
uvicorn main:app --reload
```

---

## Future Enhancements

- Expand dataset with more acts, clauses, and state-specific laws.
- Enhanced document analysis for contracts and agreements.
- Real-time integration with public legal APIs for updated case references.
- Multi-language support beyond English and Hindi.
- Mobile-friendly frontend and PDF upload support

 ---
 
## Acknowledgements
- CrewAI – Multi-agent orchestration
- NLP Models – Grok (Meta)
- Document Parsing – pdfminer.six, unstructured, Tesseract OCR
- Vector Databases – Chroma, FAISS, Pinecone
