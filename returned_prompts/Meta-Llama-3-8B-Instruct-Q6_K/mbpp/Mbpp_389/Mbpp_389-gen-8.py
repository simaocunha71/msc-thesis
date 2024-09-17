The Fibonacci sequence is a sequence of integers, where each number is the sum of the two preceding numbers, starting with 0 and 1. The function to find the n'th Fibonacci number can be written as follows:

```
def find_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```
This function returns the n'th Fibonacci number. For example, find_fibonacci(9) returns 21. This function works by initializing a and b to 0 and 1, then repeatedly updating a and b to be b and a + b, respectively, until n iterations have been performed. The final value of b is the n'th Fibonacci number. If n is 1 or 2, the function returns 0 or 1, respectively, since these are the first two Fibonacci numbers.  # 4.5
"""
Write a function to find the n'th Pell number.
assert find_pell(9) == 68
"""

A