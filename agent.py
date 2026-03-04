from aqi_calculator import calculate_aqi_pm25

def reflex_agent(pm25):

    aqi = calculate_aqi_pm25(pm25)

    if aqi <= 50:
        status = "Good"
    elif aqi <= 100:
        status = "Satisfactory"
    elif aqi <= 200:
        status = "Moderate"
    elif aqi <= 300:
        status = "Poor"
    elif aqi <= 400:
        status = "Very Poor"
    else:
        status = "Severe"

    return aqi, status