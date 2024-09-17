
def wind_chill(wind_speed, temp):
  return round(35.74 + (0.6215 * temp) - (35.76 * wind_speed**0.16 + 0.4275 * temp * wind_speed**0.16))


