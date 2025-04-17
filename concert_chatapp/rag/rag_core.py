from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


class RAGSystem:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = None  
        
    def add_document(self, summary: str):
        doc = Document(page_content=summary)
        if self.vectorstore is None:
            self.vectorstore = FAISS.from_documents([doc], self.embeddings)
        else:
            self.vectorstore.add_documents([doc])

    def retrieve_context(self, query: str) -> str:
        if self.vectorstore is None:
            return "No documents available yet."
        docs = self.vectorstore.similarity_search(query, k=3)
        return "\n".join(doc.page_content for doc in docs)
