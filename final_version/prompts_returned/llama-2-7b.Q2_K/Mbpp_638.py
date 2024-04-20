"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
import math
def wind_chill(wind_velocity, temp):
	if type(wind_velocity) == int: return wind_chill(round((wind_velocity)), round(temp))
    return 35.8 + 0.6215 * math.pow(math.cosh(math.log(wind_velocity/9.8, temp)/math.LN10), -0.4)
