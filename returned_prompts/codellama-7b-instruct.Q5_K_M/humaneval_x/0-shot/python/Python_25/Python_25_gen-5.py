from typing import List


def factorize(n: int) -> List[int]:
    if n == 1:
        return [1]
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n != 1:
        factors.append(n)
    return factors


def factorize(n: int) -> List[int]:
    if n == 1:
        return [1]
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n != 1:
        factors.append(n)
    return factors
