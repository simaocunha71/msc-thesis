def wind_chill(wind_velocity, temperature):
    return int(35.74 + 0.6215 * wind_velocity - 35.75 * (temperature**0.16) + 0.4275 * (temperature**0.16) * (wind_velocity**0.16))