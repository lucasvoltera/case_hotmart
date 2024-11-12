from bs4 import BeautifulSoup
import requests
from config import logger

def scrape_and_extract_paragraphs(url: str):
    logger.info(f"Realizando scraping da URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    paragraphs = soup.find_all('p')
    logger.info(f"{len(paragraphs)} parágrafos encontrados.")
    return [p.get_text() for p in paragraphs]
