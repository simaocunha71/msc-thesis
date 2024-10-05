    def is_prime(n: int) -> bool:
        """Return True if n is a prime number."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n):
        while n % i == 0:
            factors.append(i)
            n //= i
        if n == 1:
            break
    return max(factors)


