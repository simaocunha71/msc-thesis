    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    factors = set()
    for i in range(2, n):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    factors.add(n)
    return max([k for k in factors if is_prime(k)]) if factors else None


