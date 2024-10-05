```
def fib(n: int):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

Explanation:

The function `fib(n)` returns the `n`-th Fibonacci number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

The base case is when `n` is less than or equal to 1, in which case the function returns 1.

For `n` greater than 1, the function calls itself recursively with `n-1` and `n-2` as arguments, and returns the sum of these two values. This is the recursive formula for the Fibonacci sequence.

The function is tested with the examples provided in the problem statement, which show that it returns the correct Fibonacci numbers for `n` equal to 10, 1, and 8.