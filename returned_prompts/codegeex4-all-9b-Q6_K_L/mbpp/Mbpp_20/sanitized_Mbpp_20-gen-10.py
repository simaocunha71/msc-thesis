def is_woodall(n):
    def factors(n):
        i = 1
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n / i == i:
                    factors.append(i)
                else:
                    factors.append(i)
                    factors.append(n // i)
                i += 1
        return factors

    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n % 2 == 0: return False
        if n < 9: return True
        if n % 3 == 0: return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f + 2) == 0: return False
            f += 6
        return True

    if n <= 0:
        return False

    if not is_prime(n):
        return False

    sum_of_factors = sum(factors(n))
    if sum_of_factors == n:
        return True
    else:
        return False