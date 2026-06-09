# src/api/polymarket_client.py
import requests
from src.logger import logger

BASE_URL = "https://data-api.polymarket.com/v1"

def buscar_leaderboard():
    """
    Busca o ranking dos melhores traders da Polymarket.
    """
    url = f"{BASE_URL}/leaderboard"
    logger.info("Buscando leaderboard da Polymarket...")
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        logger.info(f"Leaderboard obtido com sucesso: {len(dados)} traders encontrados")
        return dados
    except Exception as erro:
        logger.error(f"Erro ao buscar leaderboard: {erro}")
        return []

def buscar_posicoes_do_trader(carteira):
    """
    Busca todas as posições abertas de um trader específico.
    """
    url = f"{BASE_URL}/positions"
    parametros = {"user": carteira}
    logger.info(f"Buscando posições do trader {carteira[:10]}...")

    try:
        resposta = requests.get(url, params=parametros)
        dados = resposta.json()
        logger.info(f"Posições obtidas: {len(dados)} posições encontradas")
        return dados
    except Exception as erro:
        logger.error(f"Erro ao buscar posições do trader {carteira[:10]}: {erro}")
        return []