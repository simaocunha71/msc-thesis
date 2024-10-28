def wind_chill(wind_speed, temp):
    wind_chill_index = (33.77 + (0.6215 * temp) + (0.4275 * wind_speed) - (0.135 * temp * wind_speed))
    return int(wind_chill_index)
