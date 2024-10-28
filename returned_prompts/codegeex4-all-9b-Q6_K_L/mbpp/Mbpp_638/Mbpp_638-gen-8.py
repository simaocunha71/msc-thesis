def wind_chill(velocity: int, temp: int) -> int:
  if temp > 10:
    return 0
  else:
    wind_chill_index = 13.12 + 0.6215 * temp -  11.37 * velocity ** 0.16 + 0.3965 * temp * velocity ** 0.16
    return round(wind_chill_index)