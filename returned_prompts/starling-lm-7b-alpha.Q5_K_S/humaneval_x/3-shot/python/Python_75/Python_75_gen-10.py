    def is_prime(n: int) -> bool:
        """Check if the given number is prime.
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_factors(n: int) -> List[int]:
        factors = []
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors

    if a <= 0:
        return False
    factors = find_factors(a)
    if len(factors) == 3 and all(is_prime(f) for f in factors):
        return True
    return False


