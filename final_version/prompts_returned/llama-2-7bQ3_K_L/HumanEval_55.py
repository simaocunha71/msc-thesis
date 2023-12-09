

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if not (0 <= n < 34):
        raise Exception("Given integer is out of range")
    num = 1
    acc = 1
    while True:
        if not (n - 1 >= 0):
            break
        else:
            temp = num + acc
            num, acc = num * (temp % int(2**34)), acc // (temp / int(2**34))
        if n == 0 or n == 1:
            break
    return acc
