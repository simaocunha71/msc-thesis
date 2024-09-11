"""
The wind chill index is calculated as follows:

Wind chill index = -10.3 + 0.6 * (T + 10) - 0.4 * (W^0.16 + 5) * (T - 10)^0.2 + 3.5 * W^0.25

Where W is the wind velocity in km/h, T is the temperature in Celsius, and the result should be rounded to the nearest integer.
"""

def wind_chill(W, T):
    return round(-10.3 + 0.6 * (T + 10) - 0.4 * (W ** 0.16 + 5) * (T - 10) ** 0.2 + 3.5 * W ** 0.25)

# Test
print(wind_chill(120, 35))  # 40







"""

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