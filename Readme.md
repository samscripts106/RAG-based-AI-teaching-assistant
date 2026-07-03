# 🎓 RAG-Based AI Teaching Assistant

An AI-powered Teaching Assistant built using **Retrieval-Augmented Generation (RAG)** that answers students' questions based on lecture videos. The system retrieves relevant lecture content using semantic search and generates grounded responses with a Large Language Model (LLM), along with the corresponding lecture and timestamp.

---

## ✨ Features

- 🎥 Processes recorded lecture videos
- 🎙️ Converts speech to text using Whisper
- 📑 Generates timestamped transcripts
- 🧠 Creates semantic embeddings using BGE-M3
- 🔍 Retrieves relevant lecture chunks using cosine similarity
- 🤖 Generates context-aware answers using Llama 3.2
- ⏱️ Provides the relevant lecture number and timestamp

---

## 🏗️ Architecture

```
Lecture Videos
      │
      ▼
Audio Extraction
      │
      ▼
Speech-to-Text (Whisper)
      │
      ▼
Transcript Chunking
      │
      ▼
Embedding Generation (BGE-M3)
      │
      ▼
Semantic Search
      │
      ▼
Prompt Construction
      │
      ▼
Llama 3.2
      │
      ▼
Final Response
```

---

## 🛠️ Tech Stack

- Python
- Ollama
- Llama 3.2
- BGE-M3 Embedding Model
- OpenAI Whisper
- FFmpeg
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
.
├── videos/
├── audios/
├── jsons/
├── extract_audio.py
├── transcribe_audio.py
├── create_embeddings.py
├── rag_inference.py
├── embeddings.joblib
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd RAG-based-AI-teaching-assistant
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Install and start **Ollama**, then download the required models:

- `llama3.2`
- `bge-m3`

Ensure **FFmpeg** is installed and available in your system PATH.

---

## 💡 How It Works

The application converts lecture videos into timestamped transcripts, generates semantic embeddings for each transcript chunk, and stores them for retrieval.

When a user asks a question:

1. The query is converted into an embedding.
2. Semantic similarity search retrieves the most relevant transcript chunks.
3. The retrieved context is provided to the language model.
4. The model generates a grounded answer and recommends the corresponding lecture and timestamp.

---

## 🚀 Future Improvements

- FAISS Vector Database
- Streamlit Web Interface
- Support for PDFs and Documents
- Incremental Embedding Updates
- Docker Deployment

---

## 📸 Demo

PROMPT: 
<img width="2504" height="948" alt="image" src="https://github.com/user-attachments/assets/1ecd0c40-f98e-4cfe-997e-e639fb8e1dae" />



RESPONSE:
<img width="2470" height="1526" alt="image" src="https://github.com/user-attachments/assets/1a1e944a-6c71-488b-b6f8-fde3a4903269" />


---

## 👤 Author

**Samprit Datta**

If you found this project interesting, consider giving it a ⭐.
