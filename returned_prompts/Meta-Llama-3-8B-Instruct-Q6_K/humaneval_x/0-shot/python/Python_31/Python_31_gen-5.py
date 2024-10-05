def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

This is the solution. The function `is_prime(n)` takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise.

The function first checks if `n` is less than 2. If it is, the function returns `False` because prime numbers are greater than 1.

Then, the function uses a for loop to check if `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, the function returns `False` because `n` is not a prime number.

If `n` is not divisible by any of these numbers, the function returns `True` because `n` is a prime number.

The unit tests provided in the question are used to verify that the function is working correctly. For example, the test `is_prime(6)` returns `False` because 6 is not a prime number, and the test `is_prime(101)` returns `True` because 101 is a prime number.