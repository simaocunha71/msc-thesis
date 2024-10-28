```
def closest_integer(value):
    value = float(value)
    if value < 0:
        return -round(abs(value))
    else:
        return round(value)
```
This function first converts the input value to a float. Then, it checks if the value is negative. If it is, it returns the negative of the rounded absolute value of the number. If the value is not negative, it simply returns the rounded value. The `round` function in Python rounds to the nearest integer, and the `abs` function is used to get the absolute value of the number. The `round` function will round away from zero when the number is equidistant from two integers. For example, `round(14.5)` returns `15`, and `round(-14.5)` returns `-15`. This is because the `round` function rounds to the nearest integer, and when the number is equidistant from two integers, it rounds away from zero. 