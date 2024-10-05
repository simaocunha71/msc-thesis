Here is a Python function that uses dynamic programming to compute the nth element of the fib4 number sequence:

```python
def fib4(n: int):
    if n < 1:
        return 0
    fib4_table = [0, 0, 2, 0] + [0]*(n-3)
    for i in range(4, n+1):
        fib4_table[i] = fib4_table[i-1] + fib4_table[i-2] + fib4_table[i-3] + fib4_table[i-4]
    return fib4_table[n]
```

This function first initializes a list `fib4_table` with the base cases for the fib4 sequence. It then fills up the rest of the list using a loop, calculating each element as the sum of the previous four elements. Finally, it returns the nth element of the list.

This function has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n. It also avoids using recursion, as requested. You can test the function with the examples you provided to see that it returns the correct results.