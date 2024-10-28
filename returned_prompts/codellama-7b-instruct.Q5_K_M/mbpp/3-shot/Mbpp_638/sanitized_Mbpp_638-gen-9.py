def wind_chill(wind_velocity_kmh: int, temperature_celsius: int) -> int:
  wind_chill_index = 35.74 + (0.6215 * wind_velocity_kmh) - (35.76 * (temperature_celsius/0.5556)) + (0.4275 * (temperature_celsius/0.5556)**2)
  return int(round(wind_chill_index))