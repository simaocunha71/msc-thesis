The Lucas numbers are a sequence of integers defined by the recurrence relation L(0) = 2, L(1) = 1, and L(n) = L(n-1) + L(n-2) for n > 1. Here is a Python function to find the n'th Lucas number:

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

This function uses a loop to calculate the Lucas numbers iteratively, starting from L(0) = 2 and L(1) = 1, and then updating the values of a and b in each iteration. The function returns the value of the n'th Lucas number. The unit test `assert find_lucas(9) == 76` ensures that the function works correctly for the 9th Lucas number, which is indeed 76. 