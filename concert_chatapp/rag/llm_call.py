from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from ..settings.settings import GROQ_API_KEY


class LLMCall:
    def __init__(self):
      
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",  
            temperature=0.5
        )
    
    def validate_theme(self, text: str) -> bool:
        keywords = ["concert", "tour", "venue", "performance", "artist"]
        return any(kw in text.lower() for kw in keywords)

    def summarize_document(self, text: str) -> str:
        prompt = PromptTemplate(
            input_variables=["text"],
            template="Summarize the following concert tour document:\n\n{text}"
        )
        chain = prompt | self.llm
        return chain.invoke({"text": text})

    def generate_answer(self, context: str, question: str) -> str:
        template = (
            "You are a helpful assistant for answering questions about upcoming concerts, tours, and venues in 2025–2026. "
            "Use only the following pieces of context to answer the question at the end. "
            "If the context or question is not related to concert tours, performances, or venues, politely reply that it is out of scope. "
            "Do not try to answer unrelated questions or make up an answer. "
            "\n\nContext:\n{context}\n\nQuestion: {question}"
        )
        
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )
        chain = prompt | self.llm
        return chain.invoke({"context": context, "question": question})
