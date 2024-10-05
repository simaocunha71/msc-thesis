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
    def fib(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return fib(i - 1) + fib(i - 2)
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    count = 0
    i = 0
    while count < n:
        fib_num = fib(i)
        if is_prime(fib_num):
            count += 1
        i += 1
    return fib_num
```
