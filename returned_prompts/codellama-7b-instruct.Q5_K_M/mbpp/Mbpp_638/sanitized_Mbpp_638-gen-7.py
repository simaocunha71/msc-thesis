def wind_chill(wind_velocity, temperature):
    wind_chill_index = 35.74 + (0.6215*temperature) - (35.76*wind_velocity**0.16 + 0.4275*temperature*wind_velocity**0.16)
    return round(wind_chill_index)