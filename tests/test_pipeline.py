from rag.rag_pipeline import setup_pipeline
from rag.vector_db import add_documents

texts = [
    "Taylor Swift will perform at Wembley Stadium, London in July 2026.",
    "Coldplay has announced a world tour starting March 2025, covering Europe and Asia.",
]
add_documents(texts)

qa_pipeline = setup_pipeline(k=2)

question = "Where is Taylor Swift performing in 2026?"
result = qa_pipeline.invoke({"question": question})

result = qa_pipeline.invoke({"question": question})
print("Answer:", result)