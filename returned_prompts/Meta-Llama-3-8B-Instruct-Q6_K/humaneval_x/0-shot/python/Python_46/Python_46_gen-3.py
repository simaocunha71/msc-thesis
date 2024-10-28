Here is a Python function that efficiently computes the n-th element of the fib4 number sequence without using recursion:

```python
def fib4(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 0
    if n == 2:
        return 2
    a, b, c, d = 0, 0, 2, 0
    for _ in range(3, n):
        a, b, c, d = b, c, d, a + b + c
    return d
```

This function initializes the first four elements of the sequence and then iterates `n-3` times to compute the remaining elements. In each iteration, it updates the last four elements of the sequence. The final result is the `n-th` element of the sequence.

The time complexity of this function is O(n), which is efficient for large values of `n`. The space complexity is O(1), which means it uses a constant amount of space. This is because it only uses a fixed number of variables to store the last four elements of the sequence, regardless of the value of `n`. 