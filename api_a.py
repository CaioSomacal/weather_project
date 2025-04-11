from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Configuração da API B
API_B_URL = "http://localhost:5001/weather/"

@app.route('/recommendation/<city>', methods=['GET'])
def get_recommendation(city):
    """Endpoint que fornece recomendações climáticas"""
    
    # 1. Consulta à API B
    try:
        response = requests.get(f"{API_B_URL}{city}")
        if response.status_code != 200:
            return jsonify({
                "error": "Cidade não encontrada",
                "available_cities": ["SãoPaulo", "RioDeJaneiro", "PortoAlegre"]
            }), 404
            
        weather_data = response.json()
        temp = weather_data['temp']
        
    except requests.exceptions.RequestException:
        return jsonify({
            "error": "Serviço de clima indisponível"
        }), 503

    # 2. Lógica de Recomendação
    if temp > 30:
        recommendation = "Hidrate-se e use protetor solar"
    elif 15 < temp <= 30:
        recommendation = "O clima está agradável"
    else:
        recommendation = "Recomendo usar um casaco"

    # 3. Resposta Padronizada
    return jsonify({
        "city": city,
        "temperature": temp,
        "unit": "Celsius",
        "recommendation": recommendation
    })

if __name__ == '__main__':
    app.run(port=5000)