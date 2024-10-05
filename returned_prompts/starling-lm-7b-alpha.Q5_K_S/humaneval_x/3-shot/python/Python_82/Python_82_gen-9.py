    def is_prime(n):
        """ Check if a number is prime
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(len(string)):
        return True
    else:
        return False


