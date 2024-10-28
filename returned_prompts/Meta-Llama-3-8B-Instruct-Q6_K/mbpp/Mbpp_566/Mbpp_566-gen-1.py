```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```


The problem is asking to write a function that takes a non-negative integer as input and returns the sum of its digits.

The unit test `assert sum_digits(345)==12` helps to clarify that the function should return the sum of the digits of the number, not the number of digits.

The solution uses a generator expression to convert the integer to a string, iterate over each character (digit) in the string, convert each character back to an integer, and sum up all the digits. The `sum` function is used to calculate the sum of the digits.