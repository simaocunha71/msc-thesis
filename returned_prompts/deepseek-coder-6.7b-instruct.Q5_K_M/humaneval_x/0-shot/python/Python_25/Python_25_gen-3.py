from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors


print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]


# Alternative solution using while loop:
def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while (n % divisor) == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    if n != 1:
        factors.append(n)
    return factors


print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]


# Alternative solution using for loop:
def factorize(n: int) -> List[int]:
    factors = []
    for divisor in range(2, n + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        if n == 1:
            break
    return factors


print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]


# Alternative solution using a while loop with optimization:
def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while (n % divisor) == 0:
            factors.append