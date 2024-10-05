from typing import List
import math

def factorize(n: int) -> List[int]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(37))  # [37]
print(factorize(48))  # [2, 2, 2, 3]
print(factorize(100))  # [2, 2, 5, 5]
print(factorize(121))  # [11, 11]
print(factorize(196))  # [2, 2, 7, 7]
print(factorize(343))  # [7, 7, 7]
print(factorize(1))  # []


# The problem statement is asking you to write a function that takes an integer as input and returns a list of its prime factors.
# The prime factors should be in the order from smallest to largest, and each factor should be listed the number of times it appears in the factorization.

# The function should work for prime numbers as well, in which case the output will be a list with a single element, the prime number itself.

# The function should also work for numbers that are not prime, in which case the output will be a list of the prime factors of the number.

# The function should work for any positive integer input, and it should return an empty list for an input of 0.

# You can use any algorithm you like to solve this problem, but the function should be able to handle large input numbers.

# Here is a Python solution using the algorithm of trial division:

def factorize(n: int) -> List[int]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# You can test this function with the following code:

print(factorize(8))  # [