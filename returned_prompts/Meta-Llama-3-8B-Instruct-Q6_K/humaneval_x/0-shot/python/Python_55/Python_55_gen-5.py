```
def fib(n: int):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
This is a recursive implementation of the Fibonacci sequence. It works by calling itself with smaller values of n until it reaches the base case (n <= 1), at which point it returns 1. The results of these recursive calls are then combined to form the final result. However, this implementation has a time complexity of O(2^n), which makes it inefficient for large values of n.

Here is an iterative implementation of the Fibonacci sequence:
```
def fib(n: int):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b
```
This implementation has a time complexity of O(n), which makes it much more efficient for large values of n. It uses a loop to iterate from 2 to n, and at each iteration, it updates the values of a and b to be the next two numbers in the sequence. The final result is returned at the end of the loop.