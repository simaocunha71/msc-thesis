The Lucas numbers are a series of integers that are similar to the Fibonacci sequence, but with a different recurrence relation. The Lucas numbers are defined as L(0) = 2, L(1) = 1, and L(n) = L(n-1) + L(n-2) for n > 1.

Here is a Python function that calculates the n'th Lucas number:

```python
def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b
```

This function uses an iterative approach to calculate the n'th Lucas number. It starts with the base cases L(0) = 2 and L(1) = 1, and then uses a loop to calculate the subsequent Lucas numbers. The loop uses the recurrence relation L(n) = L(n-1) + L(n-2) to calculate each new Lucas number. The function returns the n'th Lucas number.

The unit test `assert find_lucas(9) == 76` ensures that the function is working correctly. The 9th Lucas number is indeed 76. You can use this function to calculate any Lucas number by passing the desired value of n as an argument. For example, `find_lucas(10)` would return the 10th Lucas number.