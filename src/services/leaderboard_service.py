# src/services/leaderboard_service.py
from src.api.polymarket_client import buscar_leaderboard, buscar_posicoes_do_trader
from src.services.categorizador import identificar_categoria
from src.logger import logger


def obter_leaderboard_completo():
    traders = buscar_leaderboard()
    resultado = []

    for trader in traders:
        trader_organizado = {
            "posicao": trader["rank"],
            "nome": trader["userName"] or "Anônimo",
            "carteira": trader["proxyWallet"],
            "lucro": round(trader["pnl"], 2),
            "volume": round(trader["vol"], 2),
            "twitter": trader["xUsername"] or "—",
        }
        resultado.append(trader_organizado)

    return resultado


def obter_categorias_do_trader(carteira):
    posicoes = buscar_posicoes_do_trader(carteira)
    categorias_encontradas = []

    for posicao in posicoes:
        titulo = posicao["title"]
        categoria = identificar_categoria(titulo)

        if categoria not in categorias_encontradas:
            categorias_encontradas.append(categoria)

    return categorias_encontradas


def filtrar_leaderboard_por_categoria(categoria_desejada):
    logger.info(f"Filtrando leaderboard por categoria: {categoria_desejada}")

    traders = obter_leaderboard_completo()
    traders_filtrados = []

    for trader in traders:
        categorias = obter_categorias_do_trader(trader["carteira"])

        if categoria_desejada in categorias:
            trader["categorias"] = categorias
            traders_filtrados.append(trader)

    return traders_filtrados


def calcular_metricas_do_trader(carteira):
    posicoes = buscar_posicoes_do_trader(carteira)

    if not posicoes:
        return None

    total_investido = sum(p["initialValue"] for p in posicoes)
    total_lucro = sum(p["cashPnl"] for p in posicoes)

    roi = (total_lucro / total_investido * 100) if total_investido > 0 else 0

    posicoes_lucrativas = sum(1 for p in posicoes if p["cashPnl"] >= 0)
    win_rate = (posicoes_lucrativas / len(posicoes) * 100) if posicoes else 0

    contagem_categorias = {}
    for posicao in posicoes:
        categoria = identificar_categoria(posicao["title"])
        contagem_categorias[categoria] = contagem_categorias.get(categoria, 0) + 1

    categoria_favorita = max(contagem_categorias, key=contagem_categorias.get)

    return {
        "total_investido": round(total_investido, 2),
        "total_lucro": round(total_lucro, 2),
        "roi": round(roi, 2),
        "win_rate": round(win_rate, 2),
        "total_posicoes": len(posicoes),
        "posicoes_lucrativas": posicoes_lucrativas,
        "categoria_favorita": categoria_favorita
    }