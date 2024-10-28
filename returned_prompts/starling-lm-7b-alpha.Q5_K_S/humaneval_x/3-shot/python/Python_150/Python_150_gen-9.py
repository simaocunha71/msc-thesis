    def is_prime(n: int) -> bool:
        """ Check if given number is prime.
        >>> is_prime(7)
        True
        >>> is_prime(15)
        False
        """
        if n < 2:
            return False
        for idx, elem in enumerate(range(2, n)):
            if n % elem == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


