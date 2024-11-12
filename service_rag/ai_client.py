import openai
import numpy as np
from config import OPENAI_API_KEY, logger

openai.api_key = OPENAI_API_KEY

# Função para vetorização usando OpenAI
def vectorize_text(text: str) -> np.ndarray:
    logger.info(f"Vetorizando o texto: {text[:60]}...")
    try:
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        embeddings = np.array(response.data[0].embedding)
        logger.info("Embedding obtido com sucesso.")
        return embeddings

    except Exception as e:
        logger.error(f"Erro ao vetorizar o texto: {e}")
        raise Exception("Falha ao obter o embedding da OpenAI.")

# Função para gerar resposta usando OpenAI
def generate_response(contexts: list, question: str) -> str:
    logger.info("Gerando resposta baseada nos contextos e na pergunta fornecida.")
    prompt = (
        f"Contexto: {contexts}\n"
        f"Pergunta: {question}\n"
        "Resposta:"
    )

    logger.info(f"Prompt gerado: {prompt}")

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        logger.info("Resposta gerada com sucesso.")
        return response.choices[0].message.content

    except Exception as e:
        logger.error(f"Erro ao gerar a resposta: {e}")
        raise Exception("Falha ao gerar resposta da OpenAI.")
