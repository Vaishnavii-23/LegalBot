🧠 Project 1: AI Legal Chatbot
ai-legal-chatbot
"Your free legal assistant. Powered by AI. Designed for India."

📌 Overview
This project is a RAG-based (Retrieval-Augmented Generation) chatbot that helps users understand legal procedures in India — from filing an FIR to applying for bail. It aims to simplify complex legal jargon using NLP, LLMs, and a searchable legal knowledge base.

🎯 Goals
Guide users step-by-step through common legal actions like FIR filing or bail requests.

Fetch answers from legal documents using semantic search + vector embeddings.

Serve both citizens and law students/legal assistants.

💡 Features
🔍 Search + Chat: Combines legal search with conversational replies.

📚 Legal Knowledge Base: Manual + scraped legal docs (where allowed).

🧠 LLM-powered RAG: Uses retrieval + generation for accurate answers.

🎨 Sleek UI: Built with React.js + Tailwind CSS.

🔒 Lightweight & Privacy-Aware: No sensitive data stored.

🛠 Tech Stack
Area	Tech Used
Frontend	React.js, Tailwind CSS
Backend	Flask or Django (TBD)
NLP & LLMs	HuggingFace Transformers, FAISS, LangChain
Vector Store	FAISS or Qdrant
Deployment	Railway / Vercel / Render
🚀 Status
🟡 Planning & Documentation Phase
📌 Working on dataset collection, RAG pipeline setup, and frontend UI.

🤝 Contributions
Open to pull requests & suggestions!
We're building this as a team project under Vaishnavi Ghuge.

📜 License
MIT License – Use it, remix it, improve it.

🩺 Project 2: Medical Diagnosis with ML
medical-diagnosis-ml
"ML for early disease prediction. Smarter diagnostics, better outcomes."

📌 Overview
A machine learning project that uses clinical data to predict the presence of diseases like diabetes or heart conditions. It focuses on clean preprocessing, model building, and explainability.

🎯 Goals
Build a clean pipeline for medical diagnosis using real-world datasets.

Train + evaluate classification models (Logistic Regression, SVM, etc.)

Highlight important features using SHAP and visualization tools.

💡 Features
📊 Clean data preprocessing (nulls, scaling, encoding)

🧠 ML model comparison (baseline to tuned)

🎯 Accuracy & F1 Score benchmarks

💬 Explainability with SHAP/feature importance

🛠 Tech Stack
Component	Tools Used
Data Analysis	Pandas, NumPy
ML Algorithms	Scikit-learn, XGBoost
Viz & Reports	Matplotlib, Seaborn
Notebook Env	Jupyter
📂 Structure
bash
Copy
Edit
medical-diagnosis-ml/
├── data/             # Cleaned datasets
├── notebooks/        # Jupyter notebooks
├── models/           # Saved models
├── utils/            # Helper functions
└── README.md
🚀 Status
🟢 Data ready and initial model built.
🔜 Working on adding SHAP explainability + hyperparameter tuning.

📜 License
Apache 2.0 License – Feel free to fork & reuse.

