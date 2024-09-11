def wind_chill(wind_velocity, temperature):
  if wind_velocity > 0 and temperature < -12.5:
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * (wind_velocity ** 0.16) + 0.4275 * temperature * (wind_velocity ** 0.16)
    return round(wind_chill_index)  # rounding the result to the next integer
  else:
    return None  # return None if wind velocity is 0 or temperature is 12.5 or more