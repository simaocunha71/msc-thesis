The given sequence is defined as follows:
Fibfib(0) = 0
Fibfib(1) = 0
Fibfib(2) = 1
Fibfib(n) = Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3) for n >= 3

Here's a Python function that efficiently computes the n-th element of the Fibfib number sequence:

```
def Fibfib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
```

This function uses an iterative approach to calculate the n-th element of the Fibfib sequence. It initializes three variables `a`, `b`, and `c` to represent the last three elements of the sequence. It then iterates from 3 to `n+1` and updates the values of `a`, `b`, and `c` based on the recurrence relation. Finally, it returns the value of `c`, which represents the n-th element of the sequence.

Here's an example usage of the function:

```
print(Fibfib(1))  # Output: 0
print(Fibfib(5))  # Output: 4
print(Fibfib(8))  # Output: 24
```

This function has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of `n`. However, for very large values of `n`, a memoized approach or a closed-form solution might be more efficient.