# ⚖️ Legal RAG Bot – Bharatiya Nyaya Sanhita (BNS)

> ⚠️ This is an experimental legal assistant and not a substitute for professional legal advice.

---

## 📌 Overview

Legal RAG Bot is a Retrieval-Augmented Generation (RAG) based chatbot designed to answer legal questions from the **Bharatiya Nyaya Sanhita (BNS)**.

It combines:

* 📄 Document ingestion (PDFs)
* 🔍 Semantic search (FAISS)
* 🤖 LLM-based answer generation

---

## 🚀 Features

* 📚 Ingest and process legal PDFs
* 🔍 Semantic retrieval using vector embeddings
* 🤖 Context-aware answer generation
* ⚖️ Legal-focused responses
* 📊 Evaluation pipeline for accuracy measurement
* 🌐 FastAPI backend for API access
* 💬 Streamlit UI for interaction

---

## 🏗️ Project Structure

```
legal-rag-bot/
│
├── data/              # Store BNS PDFs here
├── faiss_index/       # Generated vector DB (after ingestion)
│
├── app/
│   ├── main.py        # FastAPI app
│   ├── rag.py         # RAG pipeline logic
│   └── ingest.py      # Data ingestion script
│
├── eval.py            # Evaluation script
├── ui.py              # Streamlit UI
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd legal-rag-bot
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Legal Documents

Place your BNS PDF(s) inside:

```
data/
```

---

### 5. Run Ingestion

```bash
python app/ingest.py
```

This will:

* Load PDFs
* Split into chunks
* Generate embeddings
* Store them in FAISS vector database

---

### 6. Run Backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

### 7. Run UI (Optional)

```bash
streamlit run ui.py
```

---

## 🧪 Evaluation

Run evaluation script:

```bash
python eval.py
```

Features:

* Manual and automatic evaluation
* Accuracy calculation
* Helps identify weak responses

---

## 🧠 How It Works

1. User asks a legal question
2. Relevant chunks are retrieved from FAISS
3. Context is passed to LLM
4. LLM generates answer strictly based on context

---

## ⚡ Special Highlights

* ✅ **Context-Restricted Answering**
  Prevents hallucination by limiting responses to retrieved text

* 🔎 **Semantic Search**
  Uses transformer-based embeddings for better relevance

* 📊 **Evaluation Pipeline**
  Measures system accuracy (rare in beginner projects)

* 🧩 **Modular Architecture**
  Easy to extend with better models or UI

---

## ⚠️ Limitations

* Accuracy depends on retrieval quality
* May miss answers if relevant context is not retrieved
* Not a substitute for professional legal advice

---

## 🚧 Future Improvements

* 📌 Add citations in responses
* 🔄 Improve retrieval using reranking
* 🧠 Use more advanced LLMs
* 💬 Add chat history UI
* 📈 Advanced evaluation metrics

---

## 👨‍💻 Author

**Yash Agrawal**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
