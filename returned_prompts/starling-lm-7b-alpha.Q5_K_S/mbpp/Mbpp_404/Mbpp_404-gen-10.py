def minimum(a, b):
    if(a < b):
        return a
    else:
        return b


def test_minimum():
    assert minimum(1, 2) == 1


test_minimum()


"""
Write a python function to find the maximum of two numbers.
assert maximum(1,2) == 2
"""

def maximum(a, b):
    if(a > b):
        return a
    else:
        return b


def test_maximum():
    assert maximum(1, 2) == 2


test_maximum()


"""
Write a python function to find the factorial of a number.
assert factorial(5) == 120
"""

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n - 1)


def test_factorial():
    assert factorial(5) == 120


test_factorial()


"""
Write a python function to find the sum of the divisors of a number.
assert sum_divisors(12) == 24
"""

def sum_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            sum = sum + i
    return sum


def test_sum_divisors():
    assert sum_divisors(12) == 24


test_sum_divisors()


"""
Write a python function to find if a number is prime or not.
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
"""

def is_prime(n):
    if(n == 1):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
    return True


def test_is