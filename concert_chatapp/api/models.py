from pydantic import BaseModel


class IngestDocs(BaseModel):
    doc_input: str


class ChatInputs(BaseModel):
    usr_input: str
