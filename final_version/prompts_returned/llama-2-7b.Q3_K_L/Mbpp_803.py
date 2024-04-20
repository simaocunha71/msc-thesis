"""
Write a function to check whether the given number is a perfect square or not. 
assert not is_perfect_square(10)
"""

def is_perfect_square(num):
    if num % 1 != 0:
        return False
    else:
        return (num ** 0.5 ) == num