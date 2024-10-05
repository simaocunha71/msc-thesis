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
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    fib_nums = [0, 1]
    prime_fib_nums = []
    while len(prime_fib_nums) < n:
        next_fib = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_fib)
        if is_prime(next_fib):
            prime_fib_nums.append(next_fib)
    return prime_fib_nums[-1]

```
