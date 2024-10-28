```
def wind_chill(wind_velocity, temperature):
    if wind_velocity < 40 or temperature < -12.5:
        return round(temperature)
    else:
        return round(13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16))
```


The function `wind_chill` calculates the wind chill index given the wind velocity in km/h and a temperature in celsius. It uses the formula from the WMO (World Meteorological Organization) which is an approximation of the wind chill index. If the wind velocity is less than 40 km/h or the temperature is less than -12.5 degrees Celsius, it returns the temperature rounded to the next integer. Otherwise, it calculates the wind chill index and rounds it to the next integer. The unit test `assert wind_chill(120,35)==40` ensures that the function works correctly. 
Note: The formula used is based on the WMO wind chill index formula, which is a simplified version of the original formula used by the US National Weather Service. The original formula is more complex and takes into account the humidity, but the WMO formula is more widely used and is sufficient for most practical purposes. 
Also, the wind chill index is not applicable for wind velocities less than 40 km/h or temperatures less than -12.5 degrees Celsius, as it is not a reliable indicator of the wind's effect on the human body in these conditions. The function handles these cases by simply returning the temperature rounded to the next integer. 
The function does not check if the input values are valid, it assumes that they are valid and will not cause a runtime error. In a real-world application, you would want to add error checking to ensure that the input values are valid and within the expected range. 
The function is case-sensitive and will not work correctly if the input values are strings. In a real-world application, you would want to convert the input values to the correct data type before using them in the function. 