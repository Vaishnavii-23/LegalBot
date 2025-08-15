# LegalBot – AI-Powered Legal Information Chatbot

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-blue)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## **Project Overview**
LegalBot is an AI-powered chatbot designed to **make complex legal information accessible and understandable** to the general public. Legal documents, government procedures, and contracts often contain technical jargon, leaving individuals unaware of their rights and obligations. LegalBot bridges this gap by providing **plain-language explanations** in **English and Hindi**, along with references to relevant laws, sections, and procedures.

> ⚠️ **Disclaimer:** LegalBot provides **general informational guidance** only. It is **not a substitute for professional legal advice**. Users seeking personalized legal counsel should consult a licensed lawyer.

---

## **Group Members**
- Vaishnavi Ghuge 
- Mayuri Patil  
- Aditya Suryawanshi  
- Pankaj Bhise  

---

## **Key Features**
- **Bilingual Support**: Answers in both English and Hindi.
- **RAG-Based Model**: Uses Retrieval-Augmented Generation to provide accurate, context-aware responses from a curated dataset of legal processes and clauses.
- **Document Clause Analysis**: Supports analyzing contracts, rental agreements, loan contracts, and terms of service, highlighting key clauses and their meanings.
- **Act & Section Mapping**: Links explanations to relevant laws and government acts for better clarity.
- **Dynamic Retrieval**: Queries both static knowledge (LegalBot dataset) and user-uploaded legal documents.
- **User-Friendly Outputs**: Step-by-step instructions, required documents, fees, timelines, and source references.

---

## **Dataset**
**LegalBot Knowledge Base**: 100+ entries covering:

- Police & FIR processes
- Court procedures (bail, appeals, divorce, cheque bounce)
- Property & Civic matters (land registration, ration cards, Aadhaar updates)
- Business & Licenses (GST, MSME, trade licenses)
- Contracts (rental agreements, indemnity, arbitration)
- Welfare & Identification processes

**Fields included**:

- `topic_en`, `topic_hi`
- `act_and_section`
- `explanation_en`, `explanation_hi`
- `required_documents`
- `fees`, `timeline`
- `source`

---

## **Technology Stack**
- **Backend**: Python + FastAPI  
- **Frontend**: React.js / Next.js  
- **NLP / LLM**: GPT-class model (OpenAI API / Hugging Face Transformers)  
- **Retrieval & Vector DB**: Chroma, FAISS, or Pinecone  
- **Document Parsing**: pdfminer.six, unstructured, Tesseract OCR  
- **Data Format**: CSV + JSON for easy ingestion  

---

## **How It Works**
1. **User Query / Document Upload**: Users ask a question or upload a legal document.  
2. **Intent Detection**: Determines if the query is procedural or document-specific.  
3. **Retrieval**: 
   - Procedural → search LegalBot dataset  
   - Document-based → parse clauses, chunk text, retrieve relevant entries  
4. **Response Generation**: RAG model produces a clear, bilingual answer citing relevant laws and sections.  
5. **Output**: Step-by-step explanation with references to acts, required documents, fees, timelines, and sources.  

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
3. Run backend server:
```bash
uvicorn main:app --reload
```
4.Open frontend at 
```bash
http://localhost:3000 and start querying LegalBot.
```
---
## Future Enhancements
- Expand dataset to 500+ entries covering more acts, states, and clauses.
- Advanced bilingual summarization and legalese simplification.
- User feedback loop for continuous improvement.
- Mobile-friendly frontend and document upload support.
---
## Acknowledgements
- Datasets: legalTransEn_Indic, MILDSum, ILSI, CUAD
- NLP Libraries: Hugging Face Transformers, OpenAI API
- Document Parsing: pdfminer.six, unstructured, Tesseract OCR

---
## License

This project is licensed under the MIT License – see the LICENSE file for details.

---

