```
def fib(n: int):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

The function `fib(n)` calculates the `n-th` Fibonacci number. It uses an iterative approach to do so. The Fibonacci sequence is defined such that each number after the first two is the sum of the two preceding ones, usually starting with 0 and 1.

The function first checks if `n` is less than or equal to 1, in which case it returns `n` as the Fibonacci sequence starts with 0 and 1. If `n` is greater than 1, the function initializes two variables `a` and `b` to 0 and 1, respectively, which represent the first two numbers in the Fibonacci sequence. It then enters a loop that runs `n-1` times, updating the values of `a` and `b` in each iteration. In each iteration, the value of `a` is updated to the value of `b`, and the value of `b` is updated to the sum of the previous values of `a` and `b`. Finally, the function returns the value of `b`, which is the `n-th` Fibonacci number.

The unit tests provided ensure that the function works correctly for different inputs. For example, `fib(10)` returns 55, which is the 10th Fibonacci number. Similarly, `fib(1)` returns 1, which is the first Fibonacci number, and `fib(8)` returns 21, which is the 8th Fibonacci number. These tests demonstrate that the function is working correctly for different inputs.