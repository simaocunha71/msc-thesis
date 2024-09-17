```
def wind_chill(wind_velocity, temperature):
    if wind_velocity <= 0:
        return temperature
    elif temperature <= -40:
        return temperature
    else:
        wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * (wind_velocity ** 0.16) + 0.3965 * temperature * (wind_velocity ** 0.16)
        return round(wind_chill_index)
```


Explanation:
This function calculates the wind chill index using the formula provided, which takes into account the wind velocity and temperature. If the wind velocity is less than or equal to 0, or the temperature is less than or equal to -40, the function returns the temperature directly as there is no wind chill effect.

The wind chill index is calculated using the formula 13.12 + 0.6215 * temperature - 11.37 * (wind_velocity ** 0.16) + 0.3965 * temperature * (wind_velocity ** 0.16). This is then rounded to the nearest integer using the round() function.

The unit test `assert wind_chill(120,35)==40` ensures that the function works correctly for the given inputs. This test checks that the wind chill index for a wind velocity of 120 km/h and a temperature of 35°C is 40, which is the expected result.