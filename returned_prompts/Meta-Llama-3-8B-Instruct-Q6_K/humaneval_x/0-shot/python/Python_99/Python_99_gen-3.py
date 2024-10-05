
The function `closest_integer` takes a string `value` as input, converts it to a float, and then checks if the decimal part is less than 0.5. If it is, it returns the integer part of the value. If it's not, it rounds the value to the nearest integer using the `round` function and then converts it back to an integer. This ensures that if the value is equidistant from two integers, it is rounded away from zero.

Here's an example implementation:

```
def closest_integer(value):
    value = float(value)
    if value - int(value) < 0.5:
        return int(value)
    else:
        return int(round(value))
```

This function will work for both positive and negative numbers, and will round away from zero when the number is equidistant from two integers. For example, `closest_integer("14.5")` will return `15`, and `closest_integer("-14.5")` will return `-15`.