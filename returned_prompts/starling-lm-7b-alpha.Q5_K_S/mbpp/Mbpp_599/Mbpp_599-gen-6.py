def sum_average(n):
    s = int((n * (n + 1)) / 2)
    return s, s / n


def test_sum_average():
    assert sum_average(10) == (55, 5.5)


test_sum_average()


"""
The above code fails on Python 3.
In Python 3, division of integers is exact and the result is also an integer.
To ensure we get a floating point number, we need to use a float for one or both of the operands.
"""

def sum_average(n):
    s = (n * (n + 1)) / 2.
    return s, s / n


def test_sum_average():
    assert sum_average(10) == (55.0, 5.5)


test_sum_average()


"""
However, Python 3.6 introduced integer division for backslash (//),
which ensures an exact integer division with the quotient as the result.
"""

def sum_average(n):
    s = (n * (n + 1)) // 2
    return s, s / n


def test_sum_average():
    assert sum_average(10) == (55, 5.5)


test_sum_average()


"""
However, Python 3.8 introduced a new syntax for floor division and quotient,
which are now written as // and / respectively.
"""

def sum_average(n):
    s = n * (n + 1) // 2
    return s, s / n


def test_sum_average():
    assert sum_average(10) == (55, 5.5)


test_sum_average()

"""
It's possible to write the function to work with Python 2 and 3,
by using the division operator for Python 2 and the floor division operator for Python 3.
"""

def sum_average(n):
    s = n * (n + 1) // 2 if n