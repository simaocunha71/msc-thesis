minimum = lambda x,y: x if x < y else y

def test_minimum():
    assert minimum(1,2) == 1

test_minimum()

"""
Write a python function to find the maximum of two numbers.
assert maximum(1,2) == 2
"""

maximum = lambda x,y: x if x > y else y

def test_maximum():
    assert maximum(1,2) == 2

test_maximum()

"""
Write a python function to find the minimum of three numbers.
assert minimum(1,2,3) == 1
"""

minimum = lambda *args: min(args)

def test_minimum():
    assert minimum(1,2,3) == 1

test_minimum()

"""
Write a python function to find the maximum of three numbers.
assert maximum(1,2,3) == 3
"""

maximum = lambda *args: max(args)

def test_maximum():
    assert maximum(1,2,3) == 3

test_maximum()
"""
Write a python function to find the minimum of a list of numbers.
assert minimum([1,2,3]) == 1
"""

minimum = lambda *args: min(args)

def test_minimum():
    assert minimum([1,2,3]) == 1

test_minimum()

"""
Write a python function to find the maximum of a list of numbers.
assert maximum([1,2,3]) == 3
"""

maximum = lambda *args: max(args)

def test_maximum():
    assert maximum([1,2,3]) == 3

test_maximum()
"""
Write a python function to check if a number is even.
assert is_even(2) == True
assert is_even(3) == False
"""

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

