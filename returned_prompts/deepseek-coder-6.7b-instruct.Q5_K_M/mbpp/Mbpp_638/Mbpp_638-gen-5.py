
import math
def wind_chill(velocity, temperature):
    return round(13.12 + 0.6215*temperature - 11.37*(velocity**0.16) + 0.3965*temperature*(velocity**0.16))

