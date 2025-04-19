# Anastasia Butkevych - Concert ChatApp (Tech Task)

## Overview
This Python service is designed to intelligently ingest and retrieve information from documents related to 2025–2026 concert tours. Built using FastAPI for the backend and Streamlit for a simple UI, it allows users to submit concert-related documents and ask context-aware questions based on ingested data. All answers are grounded strictly in the uploaded documents, using Retrieval-Augmented Generation (RAG) powered by LangChain, Groq LLMs, and FAISS vector search.

## Main Features
**1. Document Ingestion:** Ingest text documents about concert tours.  

**2. Document Theme Validation:** Validate whether the document fits the required theme.  

**3. Summaries Generation:** Generate summaries of valid documents using a Groq-hosted LLM.  

**4. Questioning:** Answer user questions based strictly on ingested content using RAG.  

**5. Interface:** Simple UI built with Streamlit for convenient interaction.

## Routes
The backend exposes the following main routes:  

- `POST /api/v1/ingest:` Ingest a new concert tour document. Returns a summary if valid, or a warning if irrelevant.

- `POST /api/v1/query:` Ask a question related to the concert tour domain. Returns an answer based on the relevant documents.

## Document Ingestion
The ingestion pipeline includes:

- **Validation:** Verifies if the document fits the concert tour domain by checking for specific keywords and patterns.

- **Summarization:** If valid, a concise summary is generated.

- **Storage:** Documents are passed to the RAG system to enable efficient future retrieval.

If the document does not match the required domain, the user receives an informative message (e.g., *"Sorry, I cannot ingest documents with other themes."*).

## Question Answering (RAG)
The system supports document-grounded Q&A by:

- **Retrieval:** Retrieving relevant chunks from previously ingested documents.

- **Answere Generation:** Using an LLM to generate answers based on the retrieved data only.

- **Answer:** Returning precise, verifiable answers with zero hallucination beyond source material.

## Project Structure
```
concert_chatapp
├── README.md
├── requirements.txt
├── run.sh
├── setup.py
├── docker
│   └── Dockerfile
├── concert_chatapp
│   ├── api
│   │   ├── models.py        
│   │   └── routes.py         
│   ├── rag
│   │   ├── llm_call.py       
│   │   └── rag_core.py       
│   ├── settings
│   │   └── settings.py       
│   └── ui
│       └── streamlit_ui.py   
```

## Setup Instructions
**IMPORTANT:** Make sure your Groq API key is available in `.env` file.

### Run with Docker
**1. Clone the Repository**
```
git clone https://github.com/anastasia-butkevich/ProvectusInternship_AnastasiaButkevych.git
cd concert_chatapp
```

**2. Build the Docker Image**
```
docker build -f docker/Dockerfile -t concert_chatapp .
```

**3. Run the Docker Container**
```
docker run --env-file .env -p 8000:8000 -p 8501:8501 concert_chatapp
```

**4. Access the Application:**  
After running the container, you can access the application by navigating to `http://localhost:8501` in your web browser.

**5. Stopping the Application:**  
Stop the container by running:
```
docker stop <container-id>
```
or using Docker desktop.