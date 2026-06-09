# 🏆 Polymarket Tracker

Leaderboard em tempo real dos melhores traders da Polymarket, com filtros por categoria e perfil detalhado de cada trader.

## ✨ Funcionalidades

- 📊 Leaderboard com os top 25 traders da Polymarket
- 🔍 Filtros por categoria (UFC, Tênis, F1, Basquete, Crypto, Política)
- 👤 Perfil detalhado de cada trader
- 📈 Métricas avançadas: ROI, Win Rate e Categoria Favorita
- ⚡ Cache para performance otimizada
- 📝 Sistema de logs com histórico de 7 dias

## 🛠️ Tecnologias

- Python 3.14
- Flask (servidor web)
- Requests (consumo de API)
- Loguru (sistema de logs)
- Pytest (testes automatizados)

## 🚀 Como rodar localmente

**1. Clone o repositório:**
```bash
git clone https://github.com/iamluc44s/poly-tracker.git
cd poly-tracker
```

**2. Crie o ambiente virtual:**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Rode o servidor:**
```bash
python main.py
```

**5. Acesse no navegador:**
http://localhost:5000

## 🧪 Rodando os testes

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

## 📁 Estrutura do projeto
polymarket-tracker/
├── src/
│   ├── api/
│   │   └── polymarket_client.py    # Comunicação com a API da Polymarket
│   ├── services/
│   │   ├── categorizador.py        # Identificação de categorias
│   │   └── leaderboard_service.py  # Regras de negócio
│   ├── app.py                      # Servidor Flask
│   └── logger.py                   # Configuração de logs
├── templates/
│   ├── leaderboard.html            # Interface do leaderboard
│   └── trader.html                 # Interface do perfil do trader
├── tests/                          # Testes automatizados
├── logs/                           # Logs do sistema
├── main.py                         # Ponto de entrada
└── requirements.txt                # Dependências

## 📊 Cobertura de Testes

- `polymarket_client.py` → 100%
- `categorizador.py` → 100%
- `leaderboard_service.py` → 100%
- Total → 66%

## 🌐 API utilizada

Este projeto utiliza a API pública da Polymarket:
- `GET /v1/leaderboard` — Top traders
- `GET /v1/positions?user={carteira}` — Posições de um trader