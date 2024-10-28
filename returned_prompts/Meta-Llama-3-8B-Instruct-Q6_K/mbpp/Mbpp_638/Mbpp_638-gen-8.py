```
def wind_chill(wind_velocity, temperature):
    if wind_velocity < 5:
        return int(13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16))
    else:
        return int(13.12 + 0.6215*temperature - 35.75*(wind_velocity**0.16) + 0.4275*temperature*(wind_velocity**0.16))
```


The wind chill index is a formula that takes into account both the temperature and the wind speed to estimate the apparent temperature felt by the human body. 

In this problem, we are given the wind velocity in km/h and the temperature in Celsius. The formula for the wind chill index is a bit complex, so we will implement it directly.

The formula is different for wind velocities less than 5 km/h and for wind velocities greater than or equal to 5 km/h. This is because the wind chill effect is more pronounced at higher wind speeds.

The result of the formula is then rounded to the nearest integer using the int() function.

The unit test provided is `assert wind_chill(120,35)==40`, which means that the wind chill index for a wind velocity of 120 km/h and a temperature of 35°C should be 40. 

This unit test helps to ensure that our function is working correctly. If our function is not working correctly, this unit test will fail and we will know that there is a mistake in our function. 

Here is the function implementation:

```
def wind_chill(wind_velocity, temperature):
    if wind_velocity < 5:
        return int(13.12 + 0.6215*temperature - 11.37*(wind_velocity**0.16) + 0.3965*temperature*(wind_velocity**0.16))
    else:
        return int(13.12 + 0.6215*temperature - 35.75*(wind_velocity**0.16) + 0.4275*temperature*(wind_velocity**0.16))
```

This function takes two arguments, `wind_velocity` and `temperature`, and returns the wind chill index rounded to the nearest integer. The function uses the formula for the wind chill index, which is different for wind velocities less than 5 km/h and for wind velocities greater than or equal to 5 km/h. The result is