The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
  fibfib(0) == 0
  fibfib(1) == 0
  fibfib(2) == 1
  fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
  Please write a function to efficiently compute the n-th element of the fibfib number sequence.
  >>> fibfib(1)
  0
  >>> fibfib(5)
  4
  >>> fibfib(8)
  24

In order to compute the n-th element of the FibFib number sequence efficiently, we can use dynamic programming to avoid redundant computation. We can store the previously computed values in an array and use them to compute the next values. Here's a Python function that does that:

```python
def fibfib(n):
    if n < 3:
        return 0
    else:
        fib = [0, 0, 1]
        for i in range(3, n + 1):
            fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
        return fib[n]
```

This function first checks if `n` is less than 3. If it is, it directly returns 0, because the FibFib sequence starts with 0, 0, 1. Otherwise, it initializes a list `fib` with the first three values of the sequence. Then, it uses a loop to compute the next values of the sequence, starting from index 3. Finally, it returns the value at index `n` of the `fib` list, which is the `n`-th element of the FibFib sequence.

For example, if you call `fibfib(5)`, the function will return 4, and if you call `fibfib(8)`, the function will return 24.

This function has a time complexity of O(n), because it only needs to iterate through the first `n` elements of the FibFib