def wind_chill(wind: float,temp: float) -> float:
  return int(35.74 + (0.6215*wind) - (35.76*((temp/0.5556)**0.16)) + (0.4275*((temp/0.5556)**0.16)*(wind)**0.16))