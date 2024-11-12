import logging
import os
from dotenv import load_dotenv


def setup_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

logger = setup_logger()

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")

