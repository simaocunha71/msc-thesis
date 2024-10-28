def wind_chill(wind_velocity, temperature):
    if wind_velocity > 40:
        wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.3965 * temperature * wind_velocity**0.16
    else:
        wind_chill_index = temperature
    return round(wind_chill_index) if wind_chill_index < 0 else 0