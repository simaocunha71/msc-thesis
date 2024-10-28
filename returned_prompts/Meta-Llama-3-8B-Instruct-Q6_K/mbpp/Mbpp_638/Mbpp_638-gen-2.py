```
def wind_chill(wind_velocity, temperature):
    if wind_velocity < 1 or temperature < -12.8:
        return None
    return round(13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16))
```


Explanation:
The wind chill index is calculated using the formula: 13.12 + 0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16, where T is the temperature in Celsius and V is the wind velocity in km/h. The formula is only valid for temperatures below -12.8°C and wind velocities above 1 km/h. If the input values are outside this range, the function returns None. The result is then rounded to the next integer. The unit test `assert wind_chill(120,35)==40` ensures that the function is working correctly.