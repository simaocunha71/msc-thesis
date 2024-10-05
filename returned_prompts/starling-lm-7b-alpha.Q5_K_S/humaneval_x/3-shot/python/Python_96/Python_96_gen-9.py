    def is_prime(n: int) -> bool:
        """Check if a given integer is prime.
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(10)
        False
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result


