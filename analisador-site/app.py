from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests

# static_folder='static' informa ao Flask onde encontrar nosso index.html
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

BLAZE_API_URL = 'https://blaze.bet.br/api/singleplayer-originals/originals/roulette_games/recent/history/1'

# Rota principal ('/') que vai servir o nosso site
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Rota da API ('/api/results') que nosso site vai chamar
@app.route('/api/results')
def get_blaze_data():
    try
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(BLAZE_API_URL, headers=headers, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# O 'if __name__ == '__main__':' não é necessário para produção,
# pois o servidor de hospedagem (Gunicorn) cuidará de iniciar o app.