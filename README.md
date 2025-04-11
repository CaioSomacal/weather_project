# weather_project
🌦️ Weather Recommendation System - API
📋 Overview
This project consists of two interconnected APIs that provide weather data and personalized recommendations based on temperature.

API Structure
API B: Weather service (port 5001)

API A: Recommendation service (port 5000) that consumes API B

🛠️ Technologies
Python 3.x

Flask (for API construction)

Requests (for inter-API communication)

🏗️ Project Structure
Copy
weather_api/
├── api_a.py          # Recommendation API
├── api_b.py          # Weather API
├── requirements.txt  # Dependencies
└── README.md
🔌 How to Run
Install dependencies:

bash
Copy
pip install -r requirements.txt
Start API B (Weather) in one terminal:

bash
Copy
python api_b.py
Start API A (Recommendations) in another terminal:

bash
Copy
python api_a.py
📚 API Documentation
API B - Weather Service
Endpoint: GET /weather/{city}

Example:

Copy
GET http://localhost:5001/weather/SãoPaulo
Response:

json
Copy
{
  "city": "SãoPaulo",
  "temp": 25,
  "unit": "Celsius"
}
API A - Recommendation Service
Endpoint: GET /recommendation/{city}

Example:

Copy
GET http://localhost:5000/recommendation/RioDeJaneiro
Response:

json
Copy
{
  "city": "RioDeJaneiro",
  "temperature": 33,
  "unit": "Celsius",
  "recommendation": "Stay hydrated and use sunscreen"
}
🔍 Recommendation Logic
Above 30°C: "Stay hydrated and use sunscreen"

Between 15°C and 30°C: "The weather is pleasant"

15°C or below: "Recommend wearing a coat"

🌦️ Sistema de Recomendações Climáticas - API
📋 Visão Geral
Este projeto consiste em duas APIs interligadas que fornecem dados climáticos e recomendações personalizadas baseadas na temperatura.

Estrutura das APIs
API B: Serviço de clima (porta 5001)

API A: Serviço de recomendações (porta 5000) que consome a API B

🛠️ Tecnologias
Python 3.x

Flask (para construção das APIs)

Requests (para comunicação entre APIs)

🏗️ Estrutura do Projeto
Copy
weather_api/
├── api_a.py          # API de Recomendações
├── api_b.py          # API de Clima
├── requirements.txt  # Dependências
└── README.md
🔌 Como Executar
Instale as dependências:

bash
Copy
pip install -r requirements.txt
Inicie a API B (Clima) em um terminal:

bash
Copy
python api_b.py
Inicie a API A (Recomendações) em outro terminal:

bash
Copy
python api_a.py
📚 Documentação das APIs
API B - Serviço de Clima
Endpoint: GET /weather/{city}

Exemplo:

Copy
GET http://localhost:5001/weather/SãoPaulo
Resposta:

json
Copy
{
  "city": "SãoPaulo",
  "temp": 25,
  "unit": "Celsius"
}
API A - Serviço de Recomendações
Endpoint: GET /recommendation/{city}

Exemplo:

Copy
GET http://localhost:5000/recommendation/RioDeJaneiro
Resposta:

json
Copy
{
  "city": "RioDeJaneiro",
  "temperature": 33,
  "unit": "Celsius",
  "recommendation": "Hidrate-se e use protetor solar"
}
🔍 Lógica de Recomendações
Acima de 30°C: "Hidrate-se e use protetor solar"

Entre 15°C e 30°C: "O clima está agradável"

15°C ou menos: "Recomendo usar um casaco"

🧪 Testando as APIs
Use ferramentas como Postman ou comandos curl:

bash
Copy
curl http://localhost:5000/recommendation/SãoPaulo
🛑 Tratamento de Erros
200: Sucesso

404: Cidade não encontrada

503: Serviço indisponível (quando API B está offline)

📦 Dependências
Copy
Flask==2.3.2
requests==2.31.0