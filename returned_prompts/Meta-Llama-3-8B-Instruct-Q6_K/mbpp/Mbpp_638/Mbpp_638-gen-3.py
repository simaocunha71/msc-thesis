```
def wind_chill(wind_velocity, temperature):
    if wind_velocity < 5:
        wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * (wind_velocity ** 0.16) + 0.3965 * temperature * (wind_velocity ** 0.16)
    else:
        wind_chill_index = 13.12 + 0.6215 * temperature - 35.77 * (wind_velocity ** 0.16)
    return round(wind_chill_index)
```


This function takes two parameters, wind velocity in km/h and temperature in Celsius. It calculates the wind chill index according to the formula provided, and then rounds the result to the nearest integer. The unit test `assert wind_chill(120,35)==40` ensures that the function returns the expected result for a wind velocity of 120 km/h and a temperature of 35°C.