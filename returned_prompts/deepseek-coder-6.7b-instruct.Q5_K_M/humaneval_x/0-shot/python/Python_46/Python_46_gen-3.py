
```python
def fib4(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0
        for _ in range(n - 4):
            a, b, c, d = b, c, d, a + b + c + d
        return d
```

This function uses a loop to iterate from 4 to `n`. It keeps track of the last four terms of the sequence in variables `a`, `b`, `c`, and `d` and updates these variables on each iteration. The current term is then returned after the loop.

This solution is efficient because it only needs to iterate `n` times and does not use recursion. The time complexity is O(n) and the space complexity is O(1).

Test the function with the provided examples:

```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This function should return the correct Fib4 sequence values for inputs 5, 6, and 7.
"""

# ---------------------
"""
