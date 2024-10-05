    def is_prime(n: int) -> bool:
        """Check if a number is prime. If n is 1 or less, return False.
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(9)
        False
        >>> is_prime(10)
        False
        >>> is_prime(77)
        True
        >>> is_prime(81)
        False
        """

        if n == 2 or n == 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True

    while not is_prime(n):
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                n = n // factor
                break
        else:
            return n

    return n


