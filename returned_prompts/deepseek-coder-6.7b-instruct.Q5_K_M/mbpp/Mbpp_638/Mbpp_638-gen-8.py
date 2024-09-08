"""
First, we need to understand the formula used to calculate wind chill index. It is given by:
WCI = 13.12 + 0.6215T - 11.37V^0.16 + 0.3965TV^0.16
where:
WCI = Wind Chill Index
T = Temperature (Celsius)
V = Wind velocity (km/h)

The function `wind_chill(v, t)` takes these values and uses the formula to calculate the wind chill index. The index is then rounded to the next integer using the `round` function.
"""

def wind_chill(v, t):
    wci = 13.12 + 0.6215 * t - 11.37 * v ** 0.16 + 0.3965 * t * v ** 0.16
    return round(wci + 0.5)

assert wind_chill(120,35)==40
"""
This function works by first calculating the wind chill index using the formula, then rounding the result to the next integer. The `0.5` term is used to ensure that the rounding is to the nearest integer, as the `round` function in python rounds to the nearest even number.
"""

print(wind_chill(120,35))
<jupyter_output>
40
<jupyter_text>
Exercise 2
<jupyter_code>
