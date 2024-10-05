```
def truncate_number(number: float) -> float:
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```
Explanation:

This function takes a positive floating point number as input and returns its decimal part. 

First, we convert the input number to an integer using the int() function, which gives us the largest integer smaller than the given number. 

Then, we subtract this integer part from the original number to get the decimal part, which is always smaller than 1. 

Finally, we return the decimal part.

The unit test `>>> truncate_number(3.5)` demonstrates that this function correctly returns the decimal part of a given number. In this case, the output is `0.5`, which is the decimal part of `3.5`. 

This function works for any positive floating point number, not just those with a fractional part of `0.5`. For example, `truncate_number(4.25)` would return `0.25`, and `truncate_number(2.75)` would return `0.75`. 

The function does not handle negative numbers, as the problem statement specifies that the input is a positive floating point number. If you want to extend this function to handle negative numbers, you could add a check at the beginning of the function and return the negative of the decimal part if the input number is negative. 