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


# Test the function
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
print(factorize(100))  # Output: [2, 2, 5, 5]
print(factorize(121))  # Output: [11, 11]  # Output: [2, 3, 5, 7, 11, 13]
print(factorize(24))  # Output: [2, 2, 2, 3]
print(factorize(36))  # Output: [2, 2, 3, 3]
print(factorize(48))  # Output: [2, 2, 2, 2, 3]
print(factorize(60))  # Output: [2, 2, 3, 5]
print(factorize(72))  # Output: [2, 2, 2, 3, 3]
print(factorize(84))  # Output: [2, 2, 3, 7]
print(factorize(96))  # Output: [2, 2, 2, 2, 2, 2, 3]
print(factorize(100))  # Output: [2, 2, 5, 5]
print(factorize(120))  # Output: [2, 2, 2, 3, 5]  # Output: [2, 2, 2, 2, 3, 5, 7]
print(factorize(144))  # Output: [2, 2, 2, 2, 3, 3]
print(factorize(168))  # Output: [2, 2, 2, 2, 3, 7]
print(factorize(192))  # Output: [2, 2, 2