"""
from math import floor
from decimal import Decimal

def wind_chill(wind, temp):
    wind = float(wind)
    temp = float(temp)
    w = 35.74 + 0.6215*temp - 35.75*Decimal(wind)**0.16 + 0.4275*temp*Decimal(wind)**0.16
    return floor(w)

"""

def wind_chill(wind, temp):
    wind = float(wind)
    temp = float(temp)
    w = 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)
    return int(round(w))

"""

def wind_chill(wind, temp):
    wind = float(wind)
    temp = float(temp)
    w = 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)
    return int(round(w))


"""
"""

def wind_chill(wind, temp):
    wind = float(wind)
    temp = float(temp)
    w = 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)
    return floor(round(w))

"""

def wind_chill(wind, temp):
    wind = float(wind)
    temp = float(temp)
    w = 35.74 + 0.6215*temp - 35.75*(wind**0.16) + 0.4275*temp*(wind**0.16)
    return floor(round(w))

"""
"""

def wind_chill(wind, temp):
    wind = float(wind)
    temp = float(temp)
   