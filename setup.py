from setuptools import setup, find_packages


setup(
    name="concert_chatapp",
    version="0.1.0",
    description="Concert Tour RAG Application",
    author="Anastasiia Butkevych",
    author_email="anastasia.butkevych@gmail.com",  
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "langchain",
        "uvicorn[standard]",
        "langchain_groq",
        "langchain-huggingface",
        "langchain-community",
        "faiss-cpu",
        "streamlit",
        "requests",
        "python-dotenv"
    ],
    python_requires=">=3.8",
)