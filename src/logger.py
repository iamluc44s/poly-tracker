# src/logger.py
# Configuração central de logs do sistema
# O Loguru é mais simples que o logging padrão do Python

from loguru import logger
import os

# Remove o handler padrão
logger.remove()

# Cria a pasta logs se não existir
os.makedirs("logs", exist_ok=True)

# Log no terminal — mostra mensagens coloridas enquanto desenvolve
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}"
)

# Log em arquivo — guarda histórico para investigar depois
logger.add(
    sink="logs/app.log",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    rotation="1 day",    # Cria um novo arquivo todo dia
    retention="7 days",  # Guarda logs dos últimos 7 dias
    encoding="utf-8"
)