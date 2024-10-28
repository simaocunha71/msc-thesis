Here is a Python function that efficiently computes the n-th element of the fib4 number sequence using dynamic programming:

```python
def fib4(n):
    if n < 1:
        return 0
    fib4_values = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
    return fib4_values[n]
```
This function initializes an array `fib4_values` with the first four elements of the fib4 sequence. Then it iterates from 4 to n, calculating each element as the sum of the previous four elements. Finally, it returns the n-th element of the sequence.

For example, `fib4(5)` returns `4`, `fib4(6)` returns `8`, and `fib4(7)` returns `14`. This function has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n. 