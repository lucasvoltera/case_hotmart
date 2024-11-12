import hashlib

def generate_text_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()
