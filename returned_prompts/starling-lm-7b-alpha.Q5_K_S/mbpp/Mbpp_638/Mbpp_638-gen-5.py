
def wind_chill(v:int, t:int) -> int:
  return int(35.74 + 0.6215*t - 35.75*v**0.16 + 0.4275*t*v**0.16)


