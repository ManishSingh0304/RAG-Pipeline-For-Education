#  RAG Based AI Teaching Assistant

##  Overview

**RAG Based AI Teaching Assistant** is an AI-powered educational chatbot that answers students' questions from course videos using **Retrieval-Augmented Generation (RAG)**. The system converts video lectures into text, processes and stores the content as vector embeddings in a Vector Database, retrieves the most relevant information for a user's query, and generates accurate responses using **GPT-5 Nano**.

The project leverages **OpenAI Whisper** for speech-to-text transcription, vector embeddings for semantic search, and Large Language Models (LLMs) for intelligent answer generation. Whisper is a speech recognition model that can transcribe audio into text.

---

##  Project Workflow

### Step 1: Videos to Text

* Input: Educational video lectures
* Videos are converted into audio files.
* Audio is transcribed into text using **OpenAI Whisper**.
* Output: Text transcripts for each video.

### Step 2: Chunking

* Long transcripts are divided into smaller chunks.
* Each chunk contains:

  * Video Name
  * Timestamp
  * Duration
  * Text Content
* Makes retrieval faster and more accurate.

**Example Chunk**

```json
{
  "video": "lecture1.mp4",
  "timestamp": "00:23:22",
  "duration": "34 sec",
  "text": "The cat is very good..."
}
```

### Step 3: Text to Vectors

* Text chunks are converted into vector embeddings.
* Embeddings capture semantic meaning of the content.
* Generated vectors are stored in a **Vector Database** for efficient search. Embeddings represent text as numerical vectors that enable semantic search and similarity matching.

### Step 4: Query to Vectors

* User enters a question.
* The query is converted into an embedding vector using the same embedding model.
* Similarity search is performed against stored vectors.

### Step 5: RAG Setup

* Relevant chunks are retrieved from the Vector Database.
* Retrieved context is combined with the user's query.
* Context is sent to the LLM as additional knowledge.

### Step 6: Generate Response

* GPT-5 Nano generates a contextual and accurate answer.
* The response is based on retrieved lecture content rather than model memory alone.

---

##  Tools & Technologies

### Programming Language
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Python Libraries
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-000000?style=for-the-badge&logo=openai&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-FF6F00?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![OS](https://img.shields.io/badge/OS_Module-4CAF50?style=for-the-badge)
![Pathlib](https://img.shields.io/badge/Pathlib-3776AB?style=for-the-badge)

### Machine Learning & NLP
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-blueviolet?style=for-the-badge)
![Embeddings](https://img.shields.io/badge/Embeddings-Vector%20Representations-ff69b4?style=for-the-badge)
![Semantic Search](https://img.shields.io/badge/Semantic_Search-00C853?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-1E88E5?style=for-the-badge)
![Information Retrieval](https://img.shields.io/badge/Information_Retrieval-FF9800?style=for-the-badge)

### Deep Learning
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![LLM](https://img.shields.io/badge/LLM-Large%20Language%20Models-8E24AA?style=for-the-badge)

### Vector Database
![Vector Store](https://img.shields.io/badge/Vector_Store-Embedding%20Storage-009688?style=for-the-badge)
![Similarity Search](https://img.shields.io/badge/Similarity_Search-Vector%20Embeddings-3F51B5?style=for-the-badge)

### AI Models
![OpenAI Whisper](https://img.shields.io/badge/OpenAI_Whisper-Speech_to_Text-412991?style=for-the-badge&logo=openai&logoColor=white)
![GPT-5 Nano](https://img.shields.io/badge/GPT--5_Nano-Response_Generation-10A37F?style=for-the-badge&logo=openai&logoColor=white)

---

##  Project Structure

```text
RAG_Based_AI_Teaching_Assistant/
│
├── audios/
├── videos/
├── jsons/
├── newjsons/
├── whisper/
│
├── app.py
├── config.py
├── mp3_to_json.py
├── video_to_mp3.py
├── preprocess_json.py
├── merge_chunks.py
├── process_incoming.py
│
├── embeddings.joblib
├── output.json
├── prompt.txt
├── response.txt
└── README.md
```

---

##  Results

### Key Features

 Converts lecture videos into searchable knowledge

 Automatic speech-to-text transcription

 Timestamp-based content retrieval

 Semantic search using vector embeddings

 Context-aware responses using RAG

 Reduces hallucinations by grounding answers in course material

 Supports multiple educational videos

### Sample Flow

```text
Student Question
        │
        ▼
Convert Query to Vector
        │
        ▼
Search Similar Chunks
        │
        ▼
Retrieve Relevant Context
        │
        ▼
GPT-5 Nano
        │
        ▼
Generate Answer
```

---

##  How to Run

### 1. Clone Repository

```bash
git clone <repository-url>
cd RAG_Based_AI_Teaching_Assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure OpenAI API Key

Create a `.env` file or update `config.py`

```python
OPENAI_API_KEY = "your_api_key_here"
```

### 4. Convert Videos to Audio

```bash
python video_to_mp3.py
```

### 5. Generate Transcripts

```bash
python mp3_to_json.py
```

### 6. Preprocess and Chunk Data

```bash
python preprocess_json.py
python merge_chunks.py
```

### 7. Generate Embeddings

```bash
python app.py
```

### 8. Start the Assistant

```bash
python process_incoming.py
```

### 9. Ask Questions

```text
What is Machine Learning?

Explain Neural Networks.

What was discussed at timestamp 00:23:22?
```

---

##  Future Improvements

* Web-based Chat Interface
* Multi-course Support
* PDF and Notes Integration
* Real-Time Video Upload
* Conversation History
* Advanced Vector Databases (FAISS, ChromaDB, Pinecone)

---

##  Author

**Manish Singh**

B.Tech (Computer Science Engineering)

Data Analytics | Data Science | AI & Machine Learning Enthusiast

---

