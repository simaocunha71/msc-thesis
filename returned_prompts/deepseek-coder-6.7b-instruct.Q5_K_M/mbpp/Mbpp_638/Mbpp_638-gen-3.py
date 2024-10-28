
import math
def wind_chill(velocity, temp):
  return round(13.12 + 0.6215*temp - 11.37*math.pow(velocity,0.16) + 0.3965*temp*math.pow(velocity,0.16))


