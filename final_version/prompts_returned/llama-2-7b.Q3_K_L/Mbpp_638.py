"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""
from typing import Any

def wind_chill(wind: int = 79, temp: float = 7.2):
    return int((temp - 10) * (wind / 10))
