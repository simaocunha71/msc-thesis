
The Fibonacci numbers are defined by the recurrence relation

```
fib(n) = fib(n-1) + fib(n-2)
```

with initial conditions

```
fib(1) = 1
fib(2) = 1
```

We can solve this recurrence relation using dynamic programming. Here is an efficient way to implement this algorithm:

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 1:
        return 1

    if n == 2:
        return 1

    fib_n = [0]*n
    fib_n[0] = 1
    fib_n[1] = 1
    for i in range(2, n):
        fib_n[i] = fib_n[i-1] + fib_n[i-2]
    return fib_n[n-1]
```

This is a standard dynamic programming problem. Here is a general template for solving it:

1. Check for the base case, and return the result if it is applicable.
2. Create a table to store results of subproblems.
3. Fill the table using the recurrence relation.
4. Return the result from the table.

This problem can also be solved using matrix exponentiation, but the dynamic programming solution is more straightforward and easier to understand.











































































































































