```
def truncate_number(number: float) -> float:
    return number - int(number)
```



The provided unit test suggests that the function should return the decimal part of the number. The decimal part can be obtained by subtracting the integer part from the original number. This can be achieved by subtracting the integer value of the number from the number itself. 

Here's the implementation:
```
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function works by first converting the float number to an integer using the `int()` function, which effectively truncates the decimal part. Then, it subtracts this integer from the original number, effectively returning the decimal part. 

For example, if we call `truncate_number(3.5)`, the function will return `0.5`, which is the decimal part of the number. 

This solution is simple and efficient, and it passes the provided unit test. 