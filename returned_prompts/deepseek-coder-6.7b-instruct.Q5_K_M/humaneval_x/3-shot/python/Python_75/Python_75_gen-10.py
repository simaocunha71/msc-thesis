    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    factors = []
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            if is_prime(i):
                factors.append(i)
            if is_prime(a // i):
                factors.append(a // i)
    factors = list(set(factors))
    factors.sort()
    if len(factors) == 3 and factors[0] * factors[1] * factors[2] == a:
        return True
    return False

