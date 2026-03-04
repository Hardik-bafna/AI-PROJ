# AQI Reflex Agent Project

This project is an Air Quality Index (AQI) monitoring application consisting of a Python Flask backend and a Next.js frontend. The system uses a reflex agent to categorize air quality based on PM2.5 concentration levels fetched from the OpenWeather API.

## Features
* **Reflex Agent**: Categorizes AQI into levels: Good, Satisfactory, Moderate, Poor, Very Poor, and Severe.
* **Real-time Data**: Retrieves geographic coordinates and pollution data for cities using external API calls.
* **Next.js Frontend**: A modern web interface for viewing air quality status.

## Project Structure
* `app.py`: Flask server handling API routes and coordination.
* `agent.py`: Implementation of the AQI reflex agent logic.
* `aqi_calculator.py`: Contains core logic for AQI numerical calculations.
* `/aqi-frontend`: Next.js application directory.

## Setup and Installation

### 1. Backend Configuration
The backend requires an OpenWeather API key to fetch environmental data.

**Create `.env` file:**
1. In the root directory (where `app.py` is located), create a file named `.env`.
2. Add your OpenWeather API key to the file:
```env
API_KEY=your_api_key_here
```

**Run the Backend:**
```python
# Install required Python packages
pip install flask flask-cors requests python-dotenv

# Start the server
python app.py
```

The Flask server will run at http://127.0.0.1:5000

### 2. Frontend Configuration

```bash
cd aqi-frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:3000

## API Endpoints

* `GET /`: Health check to verify the API is running.

* `GET /aqi?city={city_name}`: Returns the PM2.5 level, AQI value, and air quality status for the specified city.
