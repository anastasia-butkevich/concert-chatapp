from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document 


CHROMA_PATH = "chroma_data/"

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding
)


def relevant_docs(query: str, k=3) -> list[str]:
    rel_docs = vector_db.similarity_search(query, k=k)
    return rel_docs


def add_documents(texts: list[str], metadatas=None) -> list[str]:
    if metadatas:
        docs = [Document(text, metadata=m) for text, m in zip(texts, metadatas)]
    else:
        docs = [Document(text) for text in texts]

    ids = vector_db.add_documents(docs)

    return ids
