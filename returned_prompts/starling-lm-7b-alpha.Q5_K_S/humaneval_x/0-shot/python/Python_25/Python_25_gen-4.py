    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


# Test Cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(99))  # [3, 3, 11]
print(factorize(60))  # [2, 2, 2, 3, 5]
print(factorize(30))  # [2, 3, 5]
print(factorize(1))  # []
print(factorize(120))  # [2, 2, 2, 2, 3, 5]
print(factorize(20))  # [2, 2, 5]
print(factorize(1000))  # [2, 2, 2, 5, 5]
































































































































































































