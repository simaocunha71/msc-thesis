    def is_prime(num: int) -> bool:
        """ Check if given number is prime. """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factor = n
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i):
            factor = i
    return factor

