# tests/test_polymarket_client.py
from unittest.mock import patch, Mock
from src.api.polymarket_client import buscar_leaderboard, buscar_posicoes_do_trader

# Dados falsos que simulam a resposta da API
RESPOSTA_LEADERBOARD_FALSA = [
    {"rank": "1", "userName": "Trader1", "pnl": 1000.0}
]

RESPOSTA_POSICOES_FALSA = [
    {"title": "UFC Fight Night", "cashPnl": 500.0}
]


def test_buscar_leaderboard_retorna_lista():
    """
    Testa se buscar_leaderboard retorna uma lista.
    Simula a resposta HTTP sem chamar a internet.
    """
    mock_resposta = Mock()
    mock_resposta.json.return_value = RESPOSTA_LEADERBOARD_FALSA

    with patch("src.api.polymarket_client.requests.get", return_value=mock_resposta):
        resultado = buscar_leaderboard()

        assert isinstance(resultado, list)
        assert len(resultado) == 1
        assert resultado[0]["userName"] == "Trader1"


def test_buscar_leaderboard_chama_url_correta():
    """
    Testa se a função chama a URL correta da API.
    """
    mock_resposta = Mock()
    mock_resposta.json.return_value = []

    with patch("src.api.polymarket_client.requests.get", return_value=mock_resposta) as mock_get:
        buscar_leaderboard()
        mock_get.assert_called_once_with("https://data-api.polymarket.com/v1/leaderboard")


def test_buscar_posicoes_do_trader_retorna_lista():
    """
    Testa se buscar_posicoes_do_trader retorna uma lista.
    """
    mock_resposta = Mock()
    mock_resposta.json.return_value = RESPOSTA_POSICOES_FALSA

    with patch("src.api.polymarket_client.requests.get", return_value=mock_resposta):
        resultado = buscar_posicoes_do_trader("0x123")

        assert isinstance(resultado, list)
        assert len(resultado) == 1


def test_buscar_posicoes_passa_carteira_como_parametro():
    """
    Testa se a carteira é passada corretamente como parâmetro.
    """
    mock_resposta = Mock()
    mock_resposta.json.return_value = []

    with patch("src.api.polymarket_client.requests.get", return_value=mock_resposta) as mock_get:
        buscar_posicoes_do_trader("0x123abc")
        mock_get.assert_called_once_with(
            "https://data-api.polymarket.com/v1/positions",
            params={"user": "0x123abc"}
        )