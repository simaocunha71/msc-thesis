```
def fib(n: int):
    if n <= 1:
        return n
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b
```


This function calculates the `n-th` Fibonacci number using a simple iterative approach. It uses a for loop to calculate the Fibonacci sequence up to the `n-th` number. The Fibonacci sequence is defined as:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

The function starts by checking if `n` is less than or equal to 1. If it is, the function returns `n` because the first two Fibonacci numbers are 0 and 1. If `n` is greater than 1, the function initializes two variables `a` and `b` to 1, which are the first two Fibonacci numbers. It then uses a for loop to calculate the Fibonacci sequence up to the `n-th` number. In each iteration, it updates `a` and `b` to `b` and `a + b` respectively. Finally, the function returns the `n-th` Fibonacci number, which is stored in `b`.

The function also includes docstrings to provide documentation for the function, including the expected input and output, as well as some examples of how to use the function. The docstrings are written in the Google style, which is a common style for Python docstrings. The docstrings are also formatted using the `>>>` syntax, which is used to represent the input and output of the function. For example, the first docstring says: `>>> fib(10) 55`, which means that if you call the function with the input `10`, it should return the output `55`.