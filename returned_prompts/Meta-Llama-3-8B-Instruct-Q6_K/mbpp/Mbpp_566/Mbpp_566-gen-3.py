```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```


The unit test `assert sum_digits(345)==12` suggests that the function should return the sum of the digits of the input number. 

This can be achieved by converting the input number to a string, then iterating over each character in the string (which will be a digit), converting the character back to an integer, and summing up all the digits. The `sum` function is used to calculate the sum of the digits.

This solution passes the given unit test. 

However, please note that the problem statement does not specify whether the input number is non-negative or not. If the input number can be negative, then the function should return the sum of the digits of the absolute value of the number. 

Here is the modified function that handles negative numbers:
```
def sum_digits(n):
    n = abs(n)
    return sum(int(digit) for digit in str(n))
```
This function first takes the absolute value of the input number using the `abs` function, then calculates the sum of the digits using the same approach as before. This way, the function works correctly for both positive and negative input numbers. 