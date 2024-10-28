
```python
def fibfib(n: int):
    fib = [0, 0, 1]
    if n < 3:
        return fib[n]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    return fib[n]
```

In this function, we initialize a list `fib` with the first three values of the FibFib sequence. If `n` is smaller than 3, we return the n-th value of the list. If `n` is 3 or larger, we use a for loop to calculate the n-th value of the FibFib sequence by adding the last three values of the list. The n-th value is then returned.

This function works by using dynamic programming, where we store the results of subproblems (the last three values of the sequence) to avoid redundant computation. This makes the function efficient, especially for large values of `n`.

The time complexity of this function is O(n) because we loop from 3 to `n` and each iteration takes constant time. The space complexity is also O(n) because we store the first `n` values of the sequence in a list.

Note: This function uses zero-based indexing, so `fibfib(0)` returns the first element of the sequence.

Also note: This function uses the Python built-in `list` data structure to store the sequence. If `n` is large, this could lead to a memory error. In such cases, you may want to consider using a generator function to yield the sequence one value at a time, rather than storing all `n` values in a list.

Note: This function assumes that `n` is a non-negative integer. If `n` is a negative integer, the function may not behave as expected.

Note: This function uses the Python built-in `list` data structure to store the sequence. If `n` is large, this could lead to a memory error. In such cases, you may want to consider using a generator function to yield the sequence one value at a time, rather than storing all `n` values in a list.

Note: This function assumes that `