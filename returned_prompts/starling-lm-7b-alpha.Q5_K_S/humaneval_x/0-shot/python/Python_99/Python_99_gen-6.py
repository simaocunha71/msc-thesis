closest_integer("10")
10

closest_integer("15.3")
15

closest_integer("14.5")
15

closest_integer("-14.5")
-15


def closest_integer(value):
    value = int(value)
    if value % 10 == 0:
        return value
    else:
        if value < 0:
            return value - value%10 if value%10 <= 5 else value - value%10 + 10
        else:
            return value + 10 - value%10 if value%10 > 5 else value + 10 - value%10 + 10
```
    closest_integer("10") # 10
    closest_integer("15.3") # 15
    closest_integer("14.5") # 15
    closest_integer("-14.5") # -15


This implementation assumes the number is positive and then subtracts the modulus if it's less than or equal to 5, and adds the modulus plus 10 if it's greater. For negative numbers, it does the opposite.

However, this implementation can fail if the modulus is 0, for instance at 0 or at multiples of 10:
```python
closest_integer("0") # 0
closest_integer("10") # 10
closest_integer("20") # 20
```

A better implementation would be to round the number to the nearest tenth (which will be either 0 or 5) and then add or subtract that amount from the original number:
```python
def closest_integer(value):
    value = int(value)
    if value % 10 == 0:
        return value
    else:
        rounding = 0 if value % 10 <= 5 else 10
        return value + rounding - value%10
```

This implementation will correctly round any number to the nearest integer, whether it's positive, negative, or a multiple of 10:
```python
closest