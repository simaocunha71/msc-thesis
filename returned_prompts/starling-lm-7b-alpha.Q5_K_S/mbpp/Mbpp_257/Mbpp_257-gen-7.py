def swap_numbers(a,b):
    return (b,a)

def test_swap_numbers():
    assert swap_numbers(10,20)==(20,10)

test_swap_numbers()


"""
Write a function that takes in a number and returns a string of that number with all of its digits reversed.
For example, if you pass in the number 12345, the function should return 54321.

assert reverse_number(12345)=='54321'
"""
def reverse_number(n):
    return str(n)[::-1]

def test_reverse_number():
    assert reverse_number(12345)=='54321'

test_reverse_number()

"""
Write a function that takes in a number and returns the number multiplied by itself.
For example, if you pass in the number 5, the function should return 25.

assert square_number(5)==25
"""
def square_number(n):
    return n*n

def test_square_number():
    assert square_number(5)==25

test_square_number()

"""
Write a function that takes in a number and returns a tuple with the number multiplied by itself and the number added to itself.
For example, if you pass in the number 5, the function should return (25,6).

assert double_square_number(5)==(25,6)
"""

def double_square_number(n):
    return (square_number(n),n+n)

def test_double_square_number():
    assert double_square_number(5)==(25,6)

test_double_square_number()

"""
Write a function that takes in a number and returns a tuple with the number multiplied by itself and the number subtracted from itself.
For example, if you pass in the number 5, the function should return (25,-4).

assert subtract_square_number(5)==(25,-4)
"""

def sub