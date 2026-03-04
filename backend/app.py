from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from agent import reflex_agent

app = Flask(__name__)
CORS(app)


API_KEY = "a8bc7fcc0d461539d83668ce9d7389ed"


@app.route("/")
def home():
    return "AQI Reflex Agent API Running"


@app.route("/aqi")
def get_aqi():

    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please provide a city name"})

    try:
     
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_data = requests.get(geo_url).json()

        if len(geo_data) == 0:
            return jsonify({"error": "City not found"})

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

       
        pollution_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        pollution_data = requests.get(pollution_url).json()

        components = pollution_data["list"][0]["components"]

        
        aqi, status = reflex_agent(components)

        return jsonify({
            "City": city,
            "PM25": components["pm2_5"],
            "PM10": components["pm10"],
            "NO2": components["no2"],
            "O3": components["o3"],
            "CO": components["co"],
            "AQI": aqi,
            "Status": status
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)