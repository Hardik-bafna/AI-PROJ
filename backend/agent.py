def sub_index(C, Clow, Chigh, Ilow, Ihigh):
    return ((Ihigh - Ilow) / (Chigh - Clow)) * (C - Clow) + Ilow


def pm25_aqi(c):

    if 0 <= c <= 30:
        return sub_index(c, 0, 30, 0, 50)
    elif 30 < c <= 60:
        return sub_index(c, 30, 60, 50, 100)
    elif 60 < c <= 90:
        return sub_index(c, 60, 90, 100, 200)
    elif 90 < c <= 120:
        return sub_index(c, 90, 120, 200, 300)
    elif 120 < c <= 250:
        return sub_index(c, 120, 250, 300, 400)
    else:
        return sub_index(c, 250, 350, 400, 500)



def pm10_aqi(c):

    if 0 <= c <= 50:
        return sub_index(c, 0, 50, 0, 50)
    elif 50 < c <= 100:
        return sub_index(c, 50, 100, 50, 100)
    elif 100 < c <= 250:
        return sub_index(c, 100, 250, 100, 200)
    elif 250 < c <= 350:
        return sub_index(c, 250, 350, 200, 300)
    elif 350 < c <= 430:
        return sub_index(c, 350, 430, 300, 400)
    else:
        return sub_index(c, 430, 500, 400, 500)



def no2_aqi(c):

    if 0 <= c <= 40:
        return sub_index(c, 0, 40, 0, 50)
    elif 40 < c <= 80:
        return sub_index(c, 40, 80, 50, 100)
    elif 80 < c <= 180:
        return sub_index(c, 80, 180, 100, 200)
    elif 180 < c <= 280:
        return sub_index(c, 180, 280, 200, 300)
    elif 280 < c <= 400:
        return sub_index(c, 280, 400, 300, 400)
    else:
        return sub_index(c, 400, 500, 400, 500)



def o3_aqi(c):

    if 0 <= c <= 50:
        return sub_index(c, 0, 50, 0, 50)
    elif 50 < c <= 100:
        return sub_index(c, 50, 100, 50, 100)
    elif 100 < c <= 168:
        return sub_index(c, 100, 168, 100, 200)
    elif 168 < c <= 208:
        return sub_index(c, 168, 208, 200, 300)
    elif 208 < c <= 748:
        return sub_index(c, 208, 748, 300, 400)
    else:
        return sub_index(c, 748, 1000, 400, 500)


def co_aqi(c):

    c = c / 1000  

    if 0 <= c <= 1:
        return sub_index(c, 0, 1, 0, 50)
    elif 1 < c <= 2:
        return sub_index(c, 1, 2, 50, 100)
    elif 2 < c <= 10:
        return sub_index(c, 2, 10, 100, 200)
    elif 10 < c <= 17:
        return sub_index(c, 10, 17, 200, 300)
    elif 17 < c <= 34:
        return sub_index(c, 17, 34, 300, 400)
    else:
        return sub_index(c, 34, 50, 400, 500)



def get_status(aqi):

    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"



def reflex_agent(pollutants):

    pm25 = pollutants["pm2_5"]
    pm10 = pollutants["pm10"]
    no2 = pollutants["no2"]
    o3 = pollutants["o3"]
    co = pollutants["co"]

    aqi_values = [
        pm25_aqi(pm25),
        pm10_aqi(pm10),
        no2_aqi(no2),
        o3_aqi(o3),
        co_aqi(co)
    ]

    final_aqi = max(aqi_values)

    status = get_status(final_aqi)

    return round(final_aqi), status