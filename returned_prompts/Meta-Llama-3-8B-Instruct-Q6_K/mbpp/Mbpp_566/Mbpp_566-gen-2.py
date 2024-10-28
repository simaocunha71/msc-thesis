```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```



The problem is asking you to create a function that takes a non-negative integer as an input and returns the sum of its digits. For example, if the input is 345, the output should be 12 (3+4+5).

The unit test provided, `assert sum_digits(345)==12`, helps clarify the problem by showing that the function should sum the digits of the input number. This means we can convert the integer to a string, iterate over each character in the string (which will be a digit), convert each character back to an integer, and sum them all up.

Here's the solution:
```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```
This function uses a generator expression to convert each character in the string representation of `n` to an integer, and then sums up all these integers using the built-in `sum` function. The `str(n)` part is used to convert `n` to a string, and `int(digit)` is used to convert each character back to an integer. The `sum` function then adds up all these integers and returns the result.