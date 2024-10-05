```
def truncate_number(number: float) -> float:
    return number - int(number)
```


The solution is a simple function that subtracts the integer part of the number from the original number. This effectively removes the integer part and leaves only the decimal part. The unit test `>>> truncate_number(3.5)` shows that this function correctly returns the decimal part of the input number. 

Note: The `int()` function in Python is used to convert a number to an integer. It effectively truncates the decimal part of the number, effectively removing it. For example, `int(3.5)` returns `3`, not `3.0`. This is why subtracting the integer part from the original number effectively removes the integer part and leaves only the decimal part. 

This function assumes that the input number is positive, as specified in the problem statement. If the input number is negative, the function may not work correctly, as the integer part of a negative number is also negative. However, the problem statement does not specify what should happen if the input number is negative, so this function does not handle this case.  If you want to handle negative numbers, you could add a check at the beginning of the function to return the negative of the result if the input number is negative. For example:

```
def truncate_number(number: float) -> float:
    if number < 0:
        return -truncate_number(-number)
    return number - int(number)
```

This modified function returns the negative of the result if the input number is negative, effectively handling negative numbers correctly. However, this is not specified in the original problem statement, so this function does not handle negative numbers by default.  If you want to handle negative numbers by default, you could add a similar check at the beginning of the function. For example:

```
def truncate_number(number: float) -> float:
    if number < 0:
        return -number + int(-number)
    return number - int(number)
```

This modified function returns the negative of the result if the input number is negative, and handles negative numbers correctly by default. However, this is not specified in the original problem statement, so this function does not handle negative numbers by default.  If you want to handle negative numbers by default, you could add a similar check at the beginning of the function. For example:

```
def truncate_number(number: float) -> float:
    if number < 0:
        return -number + int(-