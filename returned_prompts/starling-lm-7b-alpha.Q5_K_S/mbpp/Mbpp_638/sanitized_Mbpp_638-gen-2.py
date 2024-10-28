def wind_chill(wind_velocity, temperature):
    wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * (wind_velocity ** 0.16) + 0.3965 * temperature * (wind_velocity ** 0.16)
    return int(round(wind_chill_index))