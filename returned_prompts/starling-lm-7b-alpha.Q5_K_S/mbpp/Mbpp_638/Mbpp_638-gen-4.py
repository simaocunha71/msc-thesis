
def wind_chill(velocity, temp):
  return int(35.74 + 0.6215*temp - 35.75*((velocity**0.16) + 0.4275))


