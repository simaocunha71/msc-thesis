def wind_chill(wind_velocity: int, temperature: int) -> int:
    w = 13.12 + 0.63 * temperature - 11.37 * (wind_velocity ** 0.16) + 0.39 * temperature * (wind_velocity ** 0.16)
    return round(w)