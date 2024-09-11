"""
def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

def test_sum_digits():
    assert sum_digits(345)==12
    print("All tests passed.")

test_sum_digits()
"""

def sum_digits(n):
    return sum(map(int, str(n)))

def test_sum_digits():
    assert sum_digits(345)==12
    print("All tests passed.")

test_sum_digits()

# Another way
def sum_digits(n):
    return sum(map(int, str(n)))

def test_sum_digits():
    assert sum_digits(345)==12
    print("All tests passed.")

test_sum_digits()

# Using itertools.chain
def sum_digits(n):
    return sum(i for i in itertools.chain(*(map(int, str(n)))))

def test_sum_digits():
    assert sum_digits(345)==12
    print("All tests passed.")

test_sum_digits()

# Using reduce
from functools import reduce

def sum_digits(n):
    return reduce(lambda x, y: x + y, map(int, str(n)))

def test_sum_digits():
    assert sum_digits(345)==12
    print("All tests passed.")

test_sum_digits()

# Using operator.itemgetter
from operator import itemgetter

def sum_digits(n):
    return sum(map(itemgetter(0), (i,) for i in str(n)))

def test_sum_digits():
    assert sum_digits(345)==12
    print("All tests passed.")

test_sum_digits()

# Using itertools.product and sum
from itertools import product

def sum_digits(n):
    return sum(