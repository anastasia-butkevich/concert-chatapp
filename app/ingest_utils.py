def process_doc(doc_input: str):
    pass

def validate_doc_theme(doc_text: str) -> bool:
    keywords = ["consert", "tour", "venue", "performance"]
    return any(keyword in doc_text.lower() for keyword in keywords)