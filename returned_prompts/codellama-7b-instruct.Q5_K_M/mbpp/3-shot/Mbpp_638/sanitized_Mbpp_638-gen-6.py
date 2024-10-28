def wind_chill(wind_vel,temp):
  wind_chill_index = 35.74 + (0.6215 * wind_vel) - (35.76 * (temp/0.5556)) + (0.4275 * (wind_vel * (temp/0.5556)))
  return int(wind_chill_index)