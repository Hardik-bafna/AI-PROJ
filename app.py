from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from agent import reflex_agent

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

# Replace with your OpenWeather API key
API_KEY = os.environ['API_KEY']


@app.route("/")
def home():
    return "AQI Reflex Agent API Running"


@app.route("/aqi")
def get_aqi():

    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please provide a city name"})

    try:
        # Step 1: Get coordinates for the city
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if len(geo_data) == 0:
            return jsonify({"error": "City not found"})

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Step 2: Get air pollution data
        pollution_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        pollution_response = requests.get(pollution_url)
        pollution_data = pollution_response.json()

        pm25 = pollution_data["list"][0]["components"]["pm2_5"]

        # Step 3: Calculate AQI using reflex agent
        aqi, status = reflex_agent(pm25)

        return jsonify({
            "City": city,
            "PM25": pm25,
            "AQI": aqi,
            "Status": status
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
