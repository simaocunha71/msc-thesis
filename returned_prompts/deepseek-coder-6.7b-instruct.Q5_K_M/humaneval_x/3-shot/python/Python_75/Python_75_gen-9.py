    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            if a // i != i and is_prime(a // i):
                factors.append(a // i)

    factors.sort()
    return len(factors) >= 3 and factors[0] * factors[1] * factors[2] == a


