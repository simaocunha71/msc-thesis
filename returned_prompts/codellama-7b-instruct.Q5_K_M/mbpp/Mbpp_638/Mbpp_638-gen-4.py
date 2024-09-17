
def wind_chill(wind_speed: float, temperature: float) -> int:
  return int(((13.12 + (0.6215 * temperature) - (11.37 * wind_speed ** 0.16) + (0.3965 * temperature * wind_speed ** 0.16))**0.5))


