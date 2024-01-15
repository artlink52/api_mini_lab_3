from flask import jsonify, Flask
from utils import get_frontend_path
from config import Config
import requests


app = Flask(__name__)

@app.route('/')
def front():
    return get_frontend_path('index.html')

# Эндпоинт для получения текущей погоды для заданного города
@app.route('/current_weather/<city>', methods=['GET'])
def get_current_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.OPENWEATHERMAP_ACCESS_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data), response.status_code

# Эндпоинт для предоставления прогноза погоды на несколько дней
@app.route('/weather_forecast/<city>', methods=['GET'])
def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=5&appid={Config.OPENWEATHERMAP_ACCESS_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data), response.status_code

# Эндпоинт для предоставления прогноза погоды на 7 дней
@app.route('/weekly_weather_forecast/<city>', methods=['GET'])
def get_weekly_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=7&appid={Config.OPENWEATHERMAP_ACCESS_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data), response.status_code

if __name__ == '__main__':
    app.run(debug=True)