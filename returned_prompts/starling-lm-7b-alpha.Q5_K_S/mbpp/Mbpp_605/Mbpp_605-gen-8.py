"""
To check if a number is prime, it is sufficient to check if it is divisible by any number from 2 to the square root of the number. If it is divisible by any of these numbers, then it is not a prime number.
For example, if you want to check if 23 is prime, you can check if it is divisible by 2, 3, 4, 5, 6, ..., 11, 12. Since 23 is not divisible by any of these numbers, it is a prime number.
Here is an implementation of the above logic in Python:

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

In the above implementation, if the number is less than 2, it is not a prime number. We then iterate from 2 to the square root of the number (inclusive) and check if the number is divisible by any of these values. If it is divisible by any of these values, we return False, indicating that the number is not prime. If the number is not divisible by any of these values, we return True, indicating that the number is prime.
"""

# Here's a Python implementation of the above logic:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Here is a test to check if the implementation is correct:
assert is_prime(13) == True

# Here are some additional tests to check if the implementation is correct:
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(12) == False
assert is_prime(10) == False
assert is_prime(0) == False
assert is_prime(-1) == False
assert is