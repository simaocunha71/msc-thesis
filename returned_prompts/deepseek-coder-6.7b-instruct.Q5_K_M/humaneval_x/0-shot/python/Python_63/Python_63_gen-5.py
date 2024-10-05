
```python
def fibfib(n: int) -> int:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 0, 1]
        for i in range(3, n+1):
            fib.append(fib[i-1] + fib[i-2] + fib[i-3])
        return fib[-1]
```

This function works by initializing a list with the first three values of the sequence. It then iteratively appends new values to the list by summing the last three values in the list. The function finally returns the last element of the list.

This solution has a time complexity of O(n) and space complexity of O(n) because it uses a list to store the values of the sequence up to the n-th term.

You can test it using the following code:

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This code should produce the expected output.

The time complexity of this solution is O(n) because it performs a single loop from 3 to n, and the space complexity is also O(n) because it stores the entire sequence up to the n-th term in a list.
"""

# ---------------------
# Solution 2
# ---------------------

"""
