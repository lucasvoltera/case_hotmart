from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from utils import generate_text_hash
from config import QDRANT_URL, logger

qdrant_client = QdrantClient(url=QDRANT_URL)

def check_text_exists_in_qdrant(text: str):
    text_hash = generate_text_hash(text)
    
    # Verifica se o documento já existe com base no hash
    existing_points = qdrant_client.scroll(
        collection_name="hotmart_db",  # Coleção onde os documentos são armazenados
        scroll_filter={"must": [{"key": "hash", "match": {"value": text_hash}}]},
        limit=1
    )
    
    return bool(existing_points)

def create_qdrant_collection_if_not_exists():
    collection_name = "hotmart_db"
    collections = qdrant_client.get_collections()
    if collection_name not in [col.name for col in collections.collections]:
        logger.info(f"Criando a coleção '{collection_name}' no Qdrant.")
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )
        logger.info(f"Coleção '{collection_name}' criada com sucesso.")

create_qdrant_collection_if_not_exists()

def store_in_vector_database(vector, document_id, text):
    text_hash = generate_text_hash(text)
    

    logger.info(f"Armazenando documento ID: {document_id} no Qdrant.")
    qdrant_client.upsert(
        collection_name="hotmart_db",
        points=[
            {
                "id": document_id,
                "vector": vector.tolist(),
                "payload": {"text": text, "hash": text_hash}
            }
        ]
    )
    logger.info(f"Documento ID: {document_id} armazenado com sucesso.")