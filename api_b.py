from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

weather_data = {
    "sãopaulo": 25,       # Não usar "São Paulo" ou "SaoPaulo"
    "riodejaneiro": 33,   # Não usar "Rio de Janeiro"
    "portoalegre": 14,
    "curitiba":10,
}

@app.route("/weather/<city>", methods=["GET"])
def get_weather(city):
    """Endpoint que retorna dados climáticos para uma cidade"""
    try:
        # Padroniza o nome da cidade (case-insensitive e sem espaços)
        city_formatted = city.lower().strip().replace(" ", "")
        logger.info(f"Consultando clima para: {city_formatted}")

        if city_formatted not in weather_data:
            logger.warning(f"Cidade não encontrada: {city}")
            return jsonify({
                "error": "Cidade não encontrada",
                "available_cities": list(weather_data.keys())
            }), 404

        return jsonify({
            "city": city_formatted,
            "temp": weather_data[city_formatted],
            "unit": "Celsius",
            "source": "mock_data"
        })

    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        return jsonify({
            "error": "Erro interno no servidor",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)