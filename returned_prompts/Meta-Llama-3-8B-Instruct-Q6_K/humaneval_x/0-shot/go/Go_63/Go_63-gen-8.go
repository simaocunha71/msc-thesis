```
def fibfib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
```


Python code to compute the n-th element of the Fibfib number sequence.
The function `Fibfib(n)` takes an integer `n` as input and returns the n-th element of the Fibfib sequence.

The code uses a for loop to compute the sequence. For `n` greater than 2, it initializes `a`, `b`, `c` to 0, 0, 1 respectively. Then, it iterates from 3 to `n` (inclusive), updating `a`, `b`, `c` as `b`, `c`, `a + b + c`. Finally, it returns `c`, which is the n-th element of the sequence.

For `n` less than or equal to 1, the function returns 0, as per the definition of the Fibfib sequence. For `n` equal to 2, the function returns 1, as per the definition of the Fibfib sequence.