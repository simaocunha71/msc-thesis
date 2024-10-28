def wind_chill(wind_kmh, temperature_celsius):
    return int((35.74 + 0.6215 * temperature_celsius - 35.75 * (wind_kmh ** 0.16) + 0.4275 * temperature_celsius * (wind_kmh ** 0.16)) * 100)