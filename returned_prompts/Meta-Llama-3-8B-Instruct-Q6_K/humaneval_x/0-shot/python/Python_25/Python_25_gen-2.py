from typing import List

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
print(factorize(100))  # [2, 2, 5, 5]
print(factorize(1))  # []
print(factorize(2))  # [2]
print(factorize(3))  # [3]
print(factorize(4))  # [2, 2]
print(factorize(5))  # [5]
print(factorize(6))  # [2, 3]
print(factorize(7))  # [7]
print(factorize(8))  # [2, 2, 2]
print(factorize(9))  # [3, 3]
print(factorize(10))  # [2, 5]
print(factorize(11))  # [11]
print(factorize(12))  # [2, 2, 3]
print(factorize(13))  # [13]
print(factorize(14))  # [2, 7]
print(factorize(15))  # [3, 5]
print(factorize(16))  # [2, 2, 2, 2]
print(factorize(17))  # [17]
print(factorize(18))  # [2, 3, 3]
print(factorize(19))  # [19]
print(factorize(20))  # [2, 2, 5]
print(factorize(21))  # [3, 7]
print(factorize(22))  # [2, 11]
print(factorize(23))  # [23]
print(factorize(24))  # [2, 2, 2, 3]
print(factorize(25))  # [5, 5]
print(factorize(26))  # [2, 13]
print(factorize(27))  # [