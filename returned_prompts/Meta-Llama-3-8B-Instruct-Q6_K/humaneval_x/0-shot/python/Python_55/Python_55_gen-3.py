```
def fib(n: int):
    if n <= 1:
        return n
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```
This solution uses a simple iterative approach to calculate the nth Fibonacci number. It initializes two variables `a` and `b` to 1, then iterates from 2 to `n` (inclusive), updating `a` and `b` to `b` and `a + b` respectively at each step. Finally, it returns the value of `b`, which is the nth Fibonacci number. This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of `n`.