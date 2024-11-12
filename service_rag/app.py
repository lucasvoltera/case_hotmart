from fastapi import FastAPI, Body, HTTPException
from database import search_in_vector_database
from config import logger
from ai_client import vectorize_text, generate_response

app = FastAPI()

@app.post("/ask")
async def ask_question(question: str = Body(..., embed=True)):
    logger.info("Recebendo nova pergunta para processamento.")
    try:
        # Vetorizar a pergunta
        question_vector = vectorize_text(question)
        
        # Buscar resultados relevantes no Qdrant
        search_results = search_in_vector_database(question_vector)
        
        # Extrair o texto original de cada resultado para o contexto
        contexts = [result.payload['text'] for result in search_results]
        
        # Gerar a resposta com base nos contextos e na pergunta
        response = generate_response(contexts, question)
        
        logger.info("Pergunta processada com sucesso.")
        return {"response": response}
    
    except Exception as e:
        logger.error(f"Erro ao processar a pergunta: {e}")
        raise HTTPException(status_code=500, detail="Falha ao processar a pergunta.")
