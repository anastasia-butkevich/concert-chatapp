from fastapi import FastAPI
from .models import IngestDocs, ChatInputs
from ..rag.rag_core import RAGSystem
from ..rag.llm_call import LLMCall


app = FastAPI()
llm = LLMCall()
rag = RAGSystem()


@app.post("/ingest")
async def ingest_document(doc_input: IngestDocs):
    text = doc_input.doc_input

    if not llm.validate_theme(text):
        return {"message": "Sorry, I cannot ingest documents with other themes."}

    summary_message = llm.summarize_document(text)   
    summary_text = summary_message.content
    
    rag.add_document(text)

    return {
        "message": "Thank you for sharing! Your document has been successfully added to the database.",
        "summary": summary_text  
    }


@app.post("/chat")
async def chat(usr_input: ChatInputs):
    query = usr_input.usr_input
    context = rag.retrieve_context(query)
    if not context:
        return {"answer": "Sorry, I couldn't find any relevant information in the database."}
    answer = llm.generate_answer(context, query)
    return {"answer": answer}


@app.get("/")
def index():
    return {"status": "ok"}
