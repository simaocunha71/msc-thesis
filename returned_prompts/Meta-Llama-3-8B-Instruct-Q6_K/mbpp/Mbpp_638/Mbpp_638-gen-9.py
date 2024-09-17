```
def wind_chill(wind_velocity, temperature):
    if wind_velocity <= 0:
        return None
    if temperature < -12.5:
        return None
    wind_chill_index = 13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16)
    return round(wind_chill_index)
```







Solution:
```
def wind_chill(wind_velocity, temperature):
    if wind_velocity <= 0:
        return None
    if temperature < -12.5:
        return None
    wind_chill_index = 13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16)
    return round(wind_chill_index)
```







Explanation:
The wind chill index is calculated using the following formula:
wind_chill_index = 13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16)

The function first checks if the wind velocity is less than or equal to 0, in which case it returns None, as the wind chill index is not defined for still air.

It then checks if the temperature is less than -12.5, in which case it also returns None, as the wind chill index is not defined for temperatures below -12.5°C.

Finally, it calculates the wind chill index using the formula and rounds it to the nearest integer using the round() function.

The unit test `assert wind_chill(120,35)==40` ensures that the function returns the correct result for the given wind velocity and temperature.