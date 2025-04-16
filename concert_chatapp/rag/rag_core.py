from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables import RunnableMap, RunnableLambda
from .llm_call import vector_db
from settings.settings import GROQ_API_KEY


llm = ChatGroq(model_name="allam-2-7b", groq_api_key=GROQ_API_KEY, temperature=0.2)


def setup_pipeline(k=3):
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={'k': k})

    template = """You are a helpful assistant for answering questions about upcoming concerts, tours, venues in 2025-2026 year.
            Use only the following pieces of context to answer the question at the end.
            If you don't know the answer, just say that you don't know, don't try to make up an answer.

            {context}  

            Question: {question}
            Answer: """

    prompt_template = PromptTemplate(template=template, input_variables=["context", "question"])
    combine_docs_chain = create_stuff_documents_chain(llm, prompt_template)

    chain = (
        RunnableMap({
            "context": RunnableLambda(lambda x: retriever.invoke(x["question"])),
            "question": RunnableLambda(lambda x: x["question"])
        })
        | combine_docs_chain
    )
    return chain