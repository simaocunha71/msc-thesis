def wind_chill(temperature, velocity):
    return round(13.12 + 0.63 * temperature - 11.37 * (velocity ** 0.16) + 0.39 * temperature * (velocity ** 0.16))