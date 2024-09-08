def is_woodall(n):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def is_prime(p):
        if p < 2:
            return False
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                return False
        return True

    factors = prime_factors(n)
    return all(is_prime(f) for f in factors)