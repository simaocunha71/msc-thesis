def wind_chill(wind_velocity, temperature):
    return round(13.12 + (0.6215 * wind_velocity) - (11.37 * (temperature / 10)) + (0.3965 * (temperature / 10) ** 2) + (0.0114 * (temperature / 10) ** 3))