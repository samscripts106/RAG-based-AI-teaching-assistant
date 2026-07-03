# 🎓 RAG-Based AI Teaching Assistant

A Retrieval-Augmented Generation (RAG) based AI Teaching Assistant that answers students' questions from recorded lecture videos. The system converts lecture videos into searchable knowledge, retrieves the most relevant lecture segments using semantic search, and generates context-aware answers using a Large Language Model (LLM).

---

## 🚀 Features

- Convert lecture videos to audio using FFmpeg
- Transcribe and translate lectures using Whisper
- Generate timestamped transcript chunks
- Create semantic embeddings using BGE-M3 via Ollama
- Retrieve relevant lecture segments using cosine similarity
- Generate grounded answers using Llama 3.2
- Recommend the relevant lecture number and timestamp to the student

---

## 🛠️ Tech Stack

- Python
- FFmpeg
- OpenAI Whisper (Large-v2)
- Ollama
- BGE-M3 Embedding Model
- Llama 3.2
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
├── README.md
└── requirements.txt
```

---

## ⚙️ Workflow

### Step 1 – Add Lecture Videos

Place all lecture videos inside the `videos/` folder.

---

### Step 2 – Extract Audio

Run:

```bash
python extract_audio.py
```

This converts all lecture videos into MP3 files using FFmpeg.

---

### Step 3 – Generate Transcripts

Run:

```bash
python transcribe_audio.py
```

Whisper transcribes and translates each lecture into timestamped JSON files.

---

### Step 4 – Generate Embeddings

Run:

```bash
python create_embeddings.py
```

This converts every transcript chunk into semantic embeddings using the **BGE-M3** embedding model and stores them in `embeddings.joblib`.

---

### Step 5 – Ask Questions

Run:

```bash
python rag_inference.py
```

Enter your question in the terminal.

The system:

- Generates an embedding for the question
- Retrieves the most relevant lecture chunks
- Builds a prompt
- Sends it to Llama 3.2 via Ollama
- Returns a grounded answer with the relevant lecture number and timestamp

---

## 🧠 RAG Pipeline

```
Lecture Video
      │
      ▼
Extract Audio (FFmpeg)
      │
      ▼
Speech-to-Text (Whisper)
      │
      ▼
Timestamped JSON
      │
      ▼
Embedding Generation (BGE-M3)
      │
      ▼
embeddings.joblib
      │
──────────────────────────────
      │
User Question
      │
      ▼
Question Embedding
      │
      ▼
Cosine Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Llama 3.2
      │
      ▼
Final Answer + Lecture Timestamp
```

---

## 📌 Future Improvements

- Replace cosine similarity search with FAISS
- Add a Streamlit web interface
- Support PDF and document ingestion
- Incremental embedding updates
- Docker support

---

## 👨‍💻 Author

**Samprit Datta**

If you found this project useful, feel free to ⭐ the repository.