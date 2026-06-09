# tests/test_leaderboard_service.py
from unittest.mock import patch
from src.services.leaderboard_service import (
    obter_leaderboard_completo,
    calcular_metricas_do_trader,
    filtrar_leaderboard_por_categoria,
    obter_categorias_do_trader
)

TRADERS_FALSOS = [
    {
        "rank": "1",
        "userName": "TraderTeste",
        "proxyWallet": "0x123",
        "pnl": 10000.0,
        "vol": 50000.0,
        "xUsername": "traderteste",
        "profileImage": ""
    },
    {
        "rank": "2",
        "userName": "",
        "proxyWallet": "0x456",
        "pnl": 5000.0,
        "vol": 20000.0,
        "xUsername": "",
        "profileImage": ""
    }
]

POSICOES_FALSAS = [
    {
        "title": "UFC Fight Night: Fighter A vs Fighter B",
        "cashPnl": 500.0,
        "initialValue": 1000.0,
        "avgPrice": 0.5,
        "outcome": "Fighter A"
    },
    {
        "title": "UFC Fight Night: Fighter C vs Fighter D",
        "cashPnl": -200.0,
        "initialValue": 800.0,
        "avgPrice": 0.4,
        "outcome": "Fighter C"
    },
    {
        "title": "Roland Garros ATP: Player A vs Player B",
        "cashPnl": 300.0,
        "initialValue": 600.0,
        "avgPrice": 0.6,
        "outcome": "Player A"
    }
]


def test_obter_leaderboard_completo():
    with patch("src.services.leaderboard_service.buscar_leaderboard", return_value=TRADERS_FALSOS):
        resultado = obter_leaderboard_completo()

        assert len(resultado) == 2
        assert resultado[0]["nome"] == "TraderTeste"
        assert resultado[0]["lucro"] == 10000.0
        assert resultado[1]["nome"] == "Anônimo"


def test_trader_sem_nome_vira_anonimo():
    with patch("src.services.leaderboard_service.buscar_leaderboard", return_value=TRADERS_FALSOS):
        resultado = obter_leaderboard_completo()
        assert resultado[1]["nome"] == "Anônimo"


def test_calcular_metricas_roi():
    with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=POSICOES_FALSAS):
        metricas = calcular_metricas_do_trader("0x123")

        assert metricas["roi"] == 25.0
        assert metricas["total_posicoes"] == 3


def test_calcular_win_rate():
    with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=POSICOES_FALSAS):
        metricas = calcular_metricas_do_trader("0x123")

        assert metricas["posicoes_lucrativas"] == 2
        assert metricas["win_rate"] == 66.67


def test_categoria_favorita():
    with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=POSICOES_FALSAS):
        metricas = calcular_metricas_do_trader("0x123")

        assert metricas["categoria_favorita"] == "UFC"


def test_filtrar_leaderboard_por_categoria():
    with patch("src.services.leaderboard_service.buscar_leaderboard", return_value=TRADERS_FALSOS):
        with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=POSICOES_FALSAS):
            resultado = filtrar_leaderboard_por_categoria("UFC")

            assert len(resultado) > 0
            for trader in resultado:
                assert "UFC" in trader["categorias"]


def test_filtrar_leaderboard_categoria_inexistente():
    posicoes_sem_futebol = [
        {
            "title": "UFC Fight Night: Fighter A vs Fighter B",
            "cashPnl": 500.0,
            "initialValue": 1000.0,
            "avgPrice": 0.5,
            "outcome": "Fighter A"
        }
    ]

    with patch("src.services.leaderboard_service.buscar_leaderboard", return_value=TRADERS_FALSOS):
        with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=posicoes_sem_futebol):
            resultado = filtrar_leaderboard_por_categoria("Futebol")

            assert len(resultado) == 0


def test_obter_categorias_do_trader():
    with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=POSICOES_FALSAS):
        categorias = obter_categorias_do_trader("0x123")

        assert "UFC" in categorias
        assert "Tênis" in categorias

def test_calcular_metricas_sem_posicoes():
    """
    Testa se retorna None quando o trader não tem posições.
    """
    with patch("src.services.leaderboard_service.buscar_posicoes_do_trader", return_value=[]):
        metricas = calcular_metricas_do_trader("0x123")

        assert metricas is None        