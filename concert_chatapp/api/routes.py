from fastapi import FastAPI
from .api.models import IngestDocs, ChatInputs


app = FastAPI()


@app.post("/ingest")
async def ingest_document(doc_input: IngestDocs):
    pass

@app.post("/chat")
async def chat(usr_input: ChatInputs):
    pass


@app.get("/")
def index():
    pass