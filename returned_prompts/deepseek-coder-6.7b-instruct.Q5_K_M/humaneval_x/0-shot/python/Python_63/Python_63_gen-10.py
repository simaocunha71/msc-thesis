
```python
def fibfib(n: int) -> int:
    if n < 2:
        return 0
    elif n == 2:
        return 1

    a, b, c = 0, 0, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c

    return c
```

In this function, we use a for loop to iterate over the range of n-2. For each iteration, we update the values of a, b, and c. The final value of c is the n-th element of the fibfib sequence.


