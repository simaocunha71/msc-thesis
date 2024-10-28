def wind_chill(velocity: float, temperature: float) -> int:
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * (velocity ** 0.16) + 0.4275 * temperature * (velocity ** 0.16)
    return round(wind_chill_index)