# src/services/categorizador.py
# Este arquivo é responsável por identificar a categoria de um mercado
# Pensa nele como um "classificador" que lê o título e diz: "isso é UFC!"

# Dicionário de categorias e suas palavras-chave
# Dicionário é como uma agenda: você procura pelo nome e acha o número
CATEGORIAS = {
    "UFC": ["UFC", "ufc"],
    "Tênis": ["ATP", "WTA", "Roland Garros", "Wimbledon", "US Open", "Australian Open"],
    "Futebol": ["FIFA", "Premier League", "Champions League", "World Cup"],
    "Basquete": ["NBA", "WNBA"],
    "F1": ["Formula 1", "F1", "Grand Prix"],
    "Política": ["President", "Election", "Senate", "Congress"],
    "Crypto": ["Bitcoin", "Ethereum", "BTC", "ETH"],
}

def identificar_categoria(titulo):
    """
    Recebe o título de um mercado e retorna sua categoria.
    Se não encontrar nenhuma categoria, retorna "Outros".
    
    Exemplo:
    titulo = "UFC Fight Night: Belal Muhammad vs. Gabriel Bonfim"
    retorna = "UFC"
    """
    for categoria, palavras_chave in CATEGORIAS.items():
        for palavra in palavras_chave:
            if palavra in titulo:
                return categoria
    
    return "Outros"