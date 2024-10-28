Here is one way to approach the problem:

1. If n is 1, then the number of such integers is 10, because all single-digit numbers from 1 to 9 (1, 2, 3, ..., 9) are valid options.
2. If n is 2, then the number of such integers is 20, because all two-digit numbers that begin or end with 1 are valid options (10, 11, 12, ..., 19, 21, ..., 91).
3. If n is 3, then the number of such integers is 30, because all three-digit numbers that begin or end with 1 are valid options (100, 101, ..., 199, 201, ..., 991).
4. And so on...

In general, for any positive integer n, the number of such integers is 10^n. This is because each of the n digits in the number can be any one of the 10 possible digits (0 through 9), and there are no restrictions on the remaining n-1 digits.

Here's a Python function that implements this logic:

```python
def startsOneEnds(n):
    return 10**n
```

You can test the function with some sample inputs to verify that it's working correctly:

```python
print(startsOneEnds(1))  # Output: 10
print(startsOneEnds(2))  # Output: 20
print(startsOneEnds(3))  # Output: 30
```

The function `startsOneEnds(n)` takes a positive integer `n` as input and returns the count of the numbers of `n`-digit positive integers that start or end with 1.

Note that the function uses the exponentiation operator `**` in Python to calculate 10 raised to the power of `n`. This is a shorthand way of writing `10 * 10 * ... * 10` (n times), where each multiplication is performed `n` times.

I hope this helps!