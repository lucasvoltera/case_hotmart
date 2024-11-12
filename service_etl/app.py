from fastapi import FastAPI
from scraper import scrape_and_extract_paragraphs
from vectorization import vectorize_and_store
from database import check_text_exists_in_qdrant
from models import URLRequest
import asyncio

# Configuração do logger
from config import logger

app = FastAPI()

@app.post("/upload")
async def upload_document(request: URLRequest):
    logger.info("Iniciando processamento do upload de documento.")
    try:
        paragraphs = scrape_and_extract_paragraphs(request.url)
        tasks = [vectorize_and_store(p) for p in paragraphs]
        await asyncio.gather(*tasks)  # Processa todos os parágrafos em paralelo

        logger.info("Documento processado e armazenado com sucesso.")
        return {"message": "Documentos processados e armazenados com sucesso."}
    
    except Exception as e:
        logger.error(f"Erro durante o processamento: {e}")
        return {"error": "Falha ao processar o documento."}
