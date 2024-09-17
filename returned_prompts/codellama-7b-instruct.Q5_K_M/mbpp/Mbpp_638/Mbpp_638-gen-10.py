
def wind_chill(wind: float,temp: float) -> float:
  wind_chill_index = 35.74 + (0.6215 * temp) - (35.75 * wind ** 0.16 + 0.4275 * temp * wind ** 0.16)
  return round(wind_chill_index)


