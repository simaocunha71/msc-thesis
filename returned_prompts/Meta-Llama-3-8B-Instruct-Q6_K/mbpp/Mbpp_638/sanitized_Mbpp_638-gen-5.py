def wind_chill(wind_speed, temperature):
  if wind_speed > 60:
    wind_chill_index = 13.12 + 0.6215*temperature - 11.37*(wind_speed**0.16) + 0.3965*temperature*(wind_speed**0.16)
  else:
    wind_chill_index = temperature
  return round(wind_chill_index)