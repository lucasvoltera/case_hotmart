from qdrant_client import QdrantClient
from config import QDRANT_URL, logger
import numpy as np

qdrant_client = QdrantClient(url=QDRANT_URL)

# Função para buscar no Qdrant
def search_in_vector_database(vector: np.ndarray):
    logger.info("Realizando busca no Qdrant usando o vetor de consulta.")
    try:
        results = qdrant_client.search(
            collection_name="hotmart_db",
            query_vector=vector.tolist(),
            limit=5  # Limitar a 5 resultados
        )
        
        # Log de quantos resultados foram encontrados
        logger.info(f"{len(results)} resultados encontrados no Qdrant.")

        # Verifica se algum resultado foi encontrado
        if not results:
            logger.warning("Nenhum resultado encontrado no Qdrant para o vetor de consulta.")
        
        return results

    except Exception as e:
        logger.error(f"Erro ao buscar no Qdrant: {e}")
        raise Exception("Falha ao buscar no banco de dados Qdrant.")