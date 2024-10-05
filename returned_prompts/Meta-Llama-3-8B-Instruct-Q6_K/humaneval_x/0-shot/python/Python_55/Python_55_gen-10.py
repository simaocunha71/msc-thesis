```
def fib(n: int):
    if n <= 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
```

This function calculates the nth Fibonacci number using a loop. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function takes an integer `n` as input and returns the `n`-th Fibonacci number. If `n` is 1 or less, the function returns 1, since the first Fibonacci number is 1. Otherwise, the function initializes two variables `a` and `b` to 1, and then iterates `n-1` times, updating `a` and `b` to `b` and `a+b` respectively. Finally, the function returns `b`, which is the `n`-th Fibonacci number. The unit tests provided in the problem ensure that the function works correctly for different values of `n`.