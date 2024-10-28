def wind_chill(wind,temp):
    wind_chill_index = 35.74 + 0.6215*wind - 35.76*temp**0.16 + 0.4275*temp**0.16*wind
    return round(wind_chill_index)