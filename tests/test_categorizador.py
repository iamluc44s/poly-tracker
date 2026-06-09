# tests/test_categorizador.py
# Testes unitários para o categorizador
# Cada função que começa com "test_" é um teste automatizado

from src.services.categorizador import identificar_categoria

def test_identifica_ufc():
    """
    Testa se o categorizador reconhece mercados UFC corretamente.
    """
    titulo = "UFC Fight Night: Belal Muhammad vs. Gabriel Bonfim"
    resultado = identificar_categoria(titulo)
    assert resultado == "UFC"

def test_identifica_tenis():
    """
    Testa se o categorizador reconhece mercados de Tênis corretamente.
    """
    titulo = "Roland Garros ATP: Joao Fonseca vs Novak Djokovic"
    resultado = identificar_categoria(titulo)
    assert resultado == "Tênis"

def test_identifica_crypto():
    """
    Testa se o categorizador reconhece mercados de Crypto corretamente.
    """
    titulo = "Will Bitcoin reach $100k by end of 2025?"
    resultado = identificar_categoria(titulo)
    assert resultado == "Crypto"

def test_retorna_outros_quando_nao_reconhece():
    """
    Testa se retorna "Outros" quando não reconhece a categoria.
    """
    titulo = "Título completamente aleatório sem categoria"
    resultado = identificar_categoria(titulo)
    assert resultado == "Outros"

def test_identifica_f1():
    """
    Testa se o categorizador reconhece mercados de F1 corretamente.
    """
    titulo = "F1 Grand Prix: Who will win in Monaco?"
    resultado = identificar_categoria(titulo)
    assert resultado == "F1"