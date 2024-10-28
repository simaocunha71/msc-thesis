
def wind_chill(wind_velocity: int, temperature: int) -> int:
  wind_chill_index = 35.74 + (0.6215 * wind_velocity) - (35.76 * (temperature/0.5556)) + (0.4275 * (temperature/0.5556) ** 2)
  return int(round(wind_chill_index))


