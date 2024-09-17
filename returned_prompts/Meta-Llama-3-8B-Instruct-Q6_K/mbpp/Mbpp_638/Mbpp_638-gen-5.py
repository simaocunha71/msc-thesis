```
def wind_chill(wind_velocity, temperature):
    if wind_velocity > 0 and temperature < -12.5:
        wind_chill_index = 13.12 + 0.6215 * temperature - 11.37 * wind_velocity**0.16 + 0.3965 * temperature * wind_velocity**0.16
        return round(wind_chill_index)
    else:
        return None
```







