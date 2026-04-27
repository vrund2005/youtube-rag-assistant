# 🎥 YouTube Q&A Assistant (RAG with LangChain + Groq)

## 📌 Overview

This project builds a **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about YouTube videos.

It processes video transcripts and generates **context-aware answers** using LLMs.

---

## ⚙️ How It Works

1. Extract transcript from YouTube video
2. Split text into chunks
3. Generate embeddings
4. Store in FAISS vector database
5. Retrieve relevant chunks based on query
6. Generate answer using LLM

---

## 🧠 Key Features

* Context-aware Q&A from video content
* Efficient retrieval using FAISS
* Chunking strategy for better accuracy

---

## 🛠 Tech Stack

* Python
* LangChain
* Groq (LLM)
* FAISS (Vector DB)
* YouTube Transcript API

---

## 📂 Project Structure

```bash
.
├── yt_app.ipynb
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions

1. Clone repo

```bash
git clone <your-repo-link>
cd youtube-qa-assistant
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add API key

```bash
GOOGLE_API_KEY=your_key_here
```

---

## 📊 Example Use Cases

* Summarize long videos
* Extract key insights
* Ask specific questions about content

---

## ⚠️ Limitations

* Depends on transcript availability
* No advanced reranking
* Basic retrieval strategy

---

## 🔮 Future Improvements

* Hybrid search (keyword + vector)
* Reranking models
* Multi-video knowledge base
* Caching for faster responses

---

## 👨‍💻 Author

Vrund Patel
