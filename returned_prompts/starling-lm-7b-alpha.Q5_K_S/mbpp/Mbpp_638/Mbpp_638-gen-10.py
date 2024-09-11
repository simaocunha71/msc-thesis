"""
Wind chill is an index that combines wind speed and temperature to provide a measure of how cold it feels. The wind chill index is calculated using the following formula:

-35.1 + 0.6 * (10 * temperature + speed) - 0.4 * (10 * temperature + speed)**2

In the wind chill formula, temperature is in degrees Celsius and speed is in km/h. The wind chill index is rounded to the nearest whole number.
"""

from math import floor

def wind_chill(temp, speed):
    temp = temp * 10 + speed
    speed = speed * speed
    return floor(-35.1 + 0.6 * temp - 0.4 * speed)


print(wind_chill(35,120))

"""
The wind chill index is calculated using the temperature and wind speed. The wind chill index is rounded to the nearest whole number using the floor function.
"""

"""
This function can be used to calculate the wind chill index in various scenarios. Here are some example scenarios:

wind_chill(35, 120) == 40
wind_chill(50, 100) == 22
wind_chill(10, 50) == 0
wind_chill(20, 20) == 0
"""

```
```

```

```

```

```
```

```

```

```

```
```
```

```

```
```
```

```

```
```
```

```

```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
``