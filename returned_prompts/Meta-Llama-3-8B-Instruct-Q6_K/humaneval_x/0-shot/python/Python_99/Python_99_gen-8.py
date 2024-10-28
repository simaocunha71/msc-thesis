```
def closest_integer(value):
    value = float(value)
    if value - int(value) < 0.5:
        return int(value)
    else:
        return int(value) + 1 if value > 0 else int(value) - 1
```


This function first converts the input value to a float. It then checks if the decimal part of the value is less than 0.5. If it is, the function returns the integer part of the value as it is closest to the original value.

If the decimal part is 0.5 or more, the function rounds the value away from zero. It does this by adding 1 to the integer part of the value if the original value is positive, and subtracting 1 if the original value is negative. This ensures that the function always returns the integer that is farther away from zero.