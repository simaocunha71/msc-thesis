```python


def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib_generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fibs = fib_generator()
    count = 0
    while True:
        fib = next(fibs)
        if is_prime(fib):
            count += 1
            if count == n:
                return fib

```
