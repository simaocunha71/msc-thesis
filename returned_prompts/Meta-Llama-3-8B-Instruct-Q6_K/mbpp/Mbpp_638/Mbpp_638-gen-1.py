```
def wind_chill(wind_velocity, temperature):
    if wind_velocity < 1.87 or temperature < -12.77:
        return round(temperature)
    else:
        return round(13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.3965 * temperature * wind_velocity**0.16)
```        
Explanation:
The wind chill index is calculated using the formula: 13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.3965 * temperature * wind_velocity**0.16. This formula is used to calculate the wind chill index when the wind velocity is greater than 1.87 km/h and the temperature is less than -12.77°C. If the wind velocity is less than 1.87 km/h or the temperature is not less than -12.77°C, the wind chill index is the same as the temperature. The wind chill index is then rounded to the next integer. The unit test `assert wind_chill(120,35)==40` ensures that the function returns the correct wind chill index.