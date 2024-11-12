import openai
import numpy as np
import uuid
from database import store_in_vector_database
from utils import generate_text_hash
from config import logger, OPENAI_API_KEY

# Configuração da API do OpenAI
openai.api_key = OPENAI_API_KEY 


def vectorize_text(text: str) -> np.ndarray:
    logger.info(f"Vetorizando o texto: {text[:60]}...")
    try:
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        # logger.info(f"Resposta da API: {response}")  # Log para verificar o tipo da resposta
        embeddings = np.array(response.data[0].embedding)  # Acessando 'data' e 'embedding' corretamente
        logger.info("Embedding obtido com sucesso.")
        return embeddings

    except Exception as e:
        logger.error(f"Erro ao vetorizar o texto: {e}")
        raise Exception("Falha ao obter o embedding da OpenAI.")
    
async def vectorize_and_store(paragraph):
    document_id = str(uuid.uuid4())
    vector = vectorize_text(paragraph)
    store_in_vector_database(vector, document_id, paragraph)
    logger.info(f"Documento ID: {document_id} processado e armazenado com sucesso.")
