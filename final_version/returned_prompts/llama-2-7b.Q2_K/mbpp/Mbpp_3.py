"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""

def is_not_prime(n):
    if n <= 0: return True
    elif n % 2 == 0 or n > 400: # use a large number to make the condition more strict.
        return True
    else:
        return False
    