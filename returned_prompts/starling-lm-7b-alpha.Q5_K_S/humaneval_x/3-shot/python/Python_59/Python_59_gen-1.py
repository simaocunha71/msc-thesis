    def prime_factors(n: int) -> List[int]:
        """ Return the list of prime factors of n. Return the list of prime factors of n. """
        factors = []
        while not n & 1:
            factors.append(2)
            n >>= 1

        limit = int(n ** 0.5) + 1
        for i in range(3, limit, 2):
            while not n & 1:
                factors.append(i)
                n >>= 1

        if n > 1:
            factors.append(n)
        return factors

    factors = prime_factors(n)
    return max(factors)


