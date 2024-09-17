
import math
def wind_chill(velocity, temperature):
  wci = 13.12 + 0.6215*temperature - 11.37*(velocity**0.16) + 0.3965*temperature*(velocity**0.16)
  return math.ceil(wci)


