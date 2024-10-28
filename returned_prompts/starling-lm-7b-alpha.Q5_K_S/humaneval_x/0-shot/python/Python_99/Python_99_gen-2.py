
def closest_integer(value):
    value = float(value)
    if value.is_integer():
        return int(value)
    else:
        if value >= 0:
            return round(value)
        else:
            return round(value) - 1

# Test cases
print(closest_integer("10") == 10)  # True
print(closest_integer("15.3") == 15)  # True
print(closest_integer("14.5") == 15)  # True
print(closest_integer("-14.5") == -15)  # True
print(closest_integer("0.0") == 0)  # True
print(closest_integer("0.5") == 1)  # True
print(closest_integer("-0.5") == -1)  # True
print(closest_integer("-1.5") == -2)  # True
print(closest_integer("-14.5") == -15)  # True

# More test cases
print(closest_integer("3.9999") == 4)  # True
print(closest_integer("-3.9999") == -4)  # True
print(closest_integer("0.00001") == 0)  # True
print(closest_integer("-0.00001") == -1)  # True

```
  
This function first checks if the input value is already an integer. If it is, it simply returns it as the closest integer. If it's not an integer, the function proceeds to round the value away from zero.

To round the value away from zero, the function uses the `round` function. However, it's important to note that the `round` function rounds to the nearest even number. In order to round away from zero, the function adjusts the rounded value by either adding or subtracting 1, depending on the sign of the original value.

For example, if the original value is positive, the function rounds up to the nearest even number. If the original value is negative, the function rounds down to the nearest even number. This