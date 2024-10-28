Here is the solution:

```python
def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```

This function uses recursion to calculate the nth Fibonacci number. It works by calling itself with smaller values of `n` until it reaches the base case of `n <= 1`, at which point it returns `n`. The results of these recursive calls are then combined to calculate the final result.

For example, to calculate `fib(4)`, the function would call itself with `n = 3` and `n = 2`, and then combine the results: `fib(3)` would call itself with `n = 2` and `n = 1`, and then combine the results, and so on. This process would continue until it reaches the base case, at which point it would start returning results back up the call stack.

Note that this function is not very efficient for large values of `n`, because it does a lot of repeated computation. For example, to calculate `fib(10)`, it would have to calculate `fib(9)` and `fib(8)`, and then `fib(8)` and `fib(7)`, and so on. This means that it would have to calculate `fib(8)` multiple times, which is unnecessary. There are more efficient ways to calculate Fibonacci numbers, such as using an iterative approach or memoization.