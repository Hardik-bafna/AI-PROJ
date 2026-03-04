def calculate_aqi_pm25(conc):

    breakpoints = [
        (0, 50, 0, 50),
        (51, 100, 51, 100),
        (101, 200, 101, 200),
        (201, 300, 201, 300),
        (301, 400, 301, 400),
        (401, 500, 401, 500)
    ]

    for bp_lo, bp_hi, aqi_lo, aqi_hi in breakpoints:
        if bp_lo <= conc <= bp_hi:
            aqi = ((aqi_hi - aqi_lo)/(bp_hi - bp_lo))*(conc - bp_lo) + aqi_lo
            return round(aqi)


    return 500