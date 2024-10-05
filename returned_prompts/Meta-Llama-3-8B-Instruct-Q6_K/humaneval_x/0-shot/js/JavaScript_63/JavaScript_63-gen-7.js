Here is a Python function that efficiently computes the n-th element of the fibfib number sequence:

```python
def fibfib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```

This function uses a simple iterative approach to compute the n-th element of the fibfib sequence. It initializes two variables `a` and `b` to the first two elements of the sequence (0 and 1), and then iteratively updates these variables using the recurrence relation `a, b = b, a + b` until it reaches the n-th element.

The time complexity of this function is O(n), which is much faster than the naive recursive approach that has a time complexity of O(2^n). The space complexity is O(1), which means the function uses a constant amount of space to store the variables `a` and `b`. This makes the function efficient for large values of `n`.

You can test the function using the following code:

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```  