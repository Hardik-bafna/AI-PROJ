from flask import Flask, jsonify
from flask_cors import CORS
import requests

from agent import reflex_agent

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AQI Reflex Agent API Running"

@app.route("/aqi")
def get_aqi():

    API_KEY = "a8bc7fcc0d461539d83668ce9d7389ed"

    lat = 17.3850
    lon = 78.4867

    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    # Debug print to terminal
    print(data)

    if "list" not in data:
        return jsonify({
            "error": "API response invalid",
            "response": data
        })

    pm25 = data["list"][0]["components"]["pm2_5"]

    aqi, status = reflex_agent(pm25)

    return jsonify({
        "PM25": pm25,
        "AQI": aqi,
        "Status": status
    })

if __name__ == "__main__":
    app.run(debug=True)