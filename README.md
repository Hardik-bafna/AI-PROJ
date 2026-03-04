# Air Quality Index (AQI) Reflex Agent

This project is a full-stack application that provides real-world Air Quality Index (AQI) data for any city. It utilizes a **Reflex Agent** logic in the backend to calculate the AQI based on various pollutant concentrations fetched from the OpenWeatherMap API.

## Project Structure

* **Backend**: A Flask-based Python server that handles API requests, fetches environmental data, and calculates AQI.
* **Frontend**: A modern, responsive web interface built with Next.js and Tailwind CSS.

## Key Features

* **Real-time Data**: Fetches current pollutant levels including PM2.5, PM10, $NO_2$, $O_3$, and $CO$.
* **Reflex Agent Logic**: Uses a rule-based agent to determine the final AQI category (e.g., Good, Satisfactory, Moderate, Poor, Severe) based on the highest sub-index of all pollutants.
* **Geolocation Integration**: Converts city names into geographical coordinates (Latitude/Longitude) to ensure accurate weather data retrieval.
* **Modern UI**: A dark-themed, minimalist dashboard for quick air quality checks.

## Technologies Used

### Backend
* **Python**: Core programming language.
* **Flask**: Web framework for the API.
* **Requests**: For making external API calls to OpenWeatherMap.
* **Flask-CORS**: To enable cross-origin requests from the frontend.

### Frontend
* **Next.js (v16.1.6)**: React framework for the user interface.
* **React (v19.2.3)**: For component-based UI development.
* **Tailwind CSS**: For styling and responsive design.
* **TypeScript**: For type-safe frontend development.

## Getting Started

### Backend Setup
1.  Navigate to the `backend/` directory.
2.  Install required dependencies:
    ```bash
    pip install flask flask-cors requests python-dotenv
    ```
3.  Create a .env file `backend/.env` 
4.  Run the Flask server:
    ```bash
    python app.py
    ```
    The server will start at `http://127.0.0.1:5000`.

### Frontend Setup
1.  Navigate to the `aqi-frontend/` directory.
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Run the development server:
    ```bash
    npm run dev
    ```
4.  Open [http://localhost:3000](http://localhost:3000) in your browser.

## How It Works

1.  **Input**: The user enters a city name in the frontend.
2.  **Geolocation**: The backend uses the OpenWeatherMap Geo API to find the coordinates of the city.
3.  **Pollution Data**: The backend fetches raw pollutant concentrations for those coordinates.
4.  **AQI Calculation**: The `reflex_agent` in `agent.py` calculates sub-indices for each pollutant and identifies the "final AQI" as the maximum value among them.
5.  **Status Assignment**: The agent maps the final AQI to a qualitative status (e.g., "Moderate" or "Severe").
6.  **Display**: The results are returned as a JSON object and displayed on the dashboard.
