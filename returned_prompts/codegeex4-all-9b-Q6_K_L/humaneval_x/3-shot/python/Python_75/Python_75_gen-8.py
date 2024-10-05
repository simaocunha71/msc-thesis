    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            a //= i
            factors.append(i)
    if a > 1:
        factors.append(a)

    for factor in factors:
        if not is_prime(factor):
            return False
    return True

