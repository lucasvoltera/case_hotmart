import logging
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

# Configuração do logger
def setup_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger("main")

logger = setup_logger()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
