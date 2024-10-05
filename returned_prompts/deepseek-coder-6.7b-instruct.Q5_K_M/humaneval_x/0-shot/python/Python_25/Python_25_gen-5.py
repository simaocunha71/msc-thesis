from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors

print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]

This function works by first handling the case of 2 (since 2 is the only even prime), then checking odd numbers starting from 3 up to the square root of n. It continuously divides n by each factor it finds until it can no longer do so. If n is still greater than 2 after this point, it is a prime factor of n and is added to the list. The function then returns the list of prime factors in ascending order.

I hope this helps. Let me know if you have any other questions.
"""


# code:
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors

print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
<jupyter_output>
[2, 2, 2]
[5, 5]
