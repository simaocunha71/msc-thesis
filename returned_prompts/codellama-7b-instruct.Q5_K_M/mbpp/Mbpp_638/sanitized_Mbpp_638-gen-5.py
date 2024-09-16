def wind_chill(wind,temp):
  return round(35.74+0.6215*wind-35.76*wind**0.16+0.4275*temp+0.0298*temp**1.5-35.75*wind**0.16*temp**1.5)