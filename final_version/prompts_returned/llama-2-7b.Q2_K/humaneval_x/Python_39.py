

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
    if n == 0:
        return 0
    else:
        ndiv = int(n / FIBONACCI_NUMBER * (int)(n // FIBONACCI_NUMBER))
        if not prime_helper(ndiv):
            raise ValueError("prime number is not exist!")
        f_val = fib(ndiv)
        return f_val

def fib(x: int):
    """
    This function returns the Fibonacci series of numbers.
    0, 1, 1, 2, 3, 5, 8, 13, 21…..
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    8
    >>> fib(6)
    21
    """
    return x + prev_result

def prime_helper(n: int):
    if n == 0 or n % 1 != 0:
        raise ValueError("not a prime number!")
    return True

def test():
    for i in range(9, 71, 2):
        if not fib_f(i) and i is not None:
            raise ValueError("prime number is not exist!")

if __name__ == '__main__':
    test()
