def wind_chill(wind: int,temp: int) -> int:
    if temp < -50 or temp > 10:
        return "Invalid temperature"
    elif wind < 4.8 or wind > 65:
        return "Invalid wind velocity"
    else:
        wci = 13.12 + 0.6215*temp - 11.37*math.pow(wind, 0.16) + 0.3965*temp*math.pow(wind, 0.16)
        return round(wci)


