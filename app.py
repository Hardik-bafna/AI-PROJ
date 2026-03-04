from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

from agent import reflex_agent

app = Flask(__name__)
CORS(app)   # Enables frontend to access API

# Home route
@app.route("/")
def home():
    return "AQI Reflex Agent API Running"

# AQI API route
@app.route("/aqi")
def get_aqi():

    # Read sensor data
    data = pd.read_csv("sensor_data.csv")

    # Get latest reading
    latest = data.iloc[-1]

    pm25 = latest["PM25"]

    # Run reflex agent
    aqi, status = reflex_agent(pm25) 

    return jsonify({
        "PM25": pm25,
        "AQI": aqi,
        "Status": status
    })


if __name__ == "__main__":
    app.run(debug=True)