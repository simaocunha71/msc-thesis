

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))


In this solution, we use the Euclidean algorithm to find the greatest common divisor (GCD) of two numbers. The algorithm is based on the principle that the GCD of two numbers is the same as the GCD of the remainder when the larger number is divided by the smaller number.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5

# The function works by subtracting the smaller number from the larger one until the numbers are equal. This final number is the GCD.

# In this case, we use the Euclidean algorithm, which is a more efficient method of finding the GCD.


# Alternatively, we can use the built-in function from the math module:

import math

print(math.gcd(3, 5))  # Output: 1
print(math.gcd(25, 15))  # Output: 5
"""
"""

# This function works by repeatedly subtracting the smaller number from the larger one until the numbers are equal. This final number is the greatest common divisor.

# Both of these solutions work for any two integers, not just the specific numbers given in the problem.

# This function is useful for many applications, such as in cryptography for finding the greatest common divisor of two large numbers, in number theory for finding the greatest common divisor of two numbers, and in other areas of mathematics.
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
