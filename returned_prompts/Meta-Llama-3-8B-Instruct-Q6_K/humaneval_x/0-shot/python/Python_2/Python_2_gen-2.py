```
def truncate_number(number: float) -> float:
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```


This function takes a positive floating point number as input, decomposes it into its integer and decimal parts, and returns the decimal part. The integer part is obtained by converting the number to an integer using the built-in `int()` function. The decimal part is obtained by subtracting the integer part from the original number. This ensures that the decimal part is always smaller than 1. For example, if the input is 3.5, the integer part is 3 and the decimal part is 0.5, which is returned by the function.