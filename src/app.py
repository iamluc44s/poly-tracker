# src/app.py
from flask import Flask, render_template, request
from flask_caching import Cache
from src.services.leaderboard_service import (
    obter_leaderboard_completo,
    filtrar_leaderboard_por_categoria
)

app = Flask(__name__, template_folder="../templates")

app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 300
cache = Cache(app)

CATEGORIAS_DISPONIVEIS = ["UFC", "Tênis", "Futebol", "Basquete", "F1", "Política", "Crypto"]


@app.route("/")
@cache.cached(timeout=300, query_string=True)
def pagina_leaderboard():
    categoria = request.args.get("categoria")

    if categoria and categoria in CATEGORIAS_DISPONIVEIS:
        traders = filtrar_leaderboard_por_categoria(categoria)
    else:
        traders = obter_leaderboard_completo()
        categoria = None

    return render_template(
        "leaderboard.html",
        traders=traders,
        categorias=CATEGORIAS_DISPONIVEIS,
        categoria_selecionada=categoria
    )


@app.route("/trader/<carteira>")
@cache.cached(timeout=300)
def pagina_trader(carteira):
    from src.api.polymarket_client import buscar_posicoes_do_trader
    from src.services.categorizador import identificar_categoria
    from src.services.leaderboard_service import calcular_metricas_do_trader

    traders = obter_leaderboard_completo()
    trader = next((t for t in traders if t["carteira"] == carteira), None)

    if not trader:
        return "Trader não encontrado", 404

    posicoes = buscar_posicoes_do_trader(carteira)
    for posicao in posicoes:
        posicao["categoria"] = identificar_categoria(posicao["title"])

    metricas = calcular_metricas_do_trader(carteira)

    return render_template(
        "trader.html",
        trader=trader,
        posicoes=posicoes,
        metricas=metricas
    )