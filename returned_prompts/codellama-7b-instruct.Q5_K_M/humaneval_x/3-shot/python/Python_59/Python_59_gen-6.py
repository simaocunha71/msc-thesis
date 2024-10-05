    # this is just the naive approach, which is not efficient.
    for i in range(n, 1, -1):
        if n % i == 0 and is_prime(i):
            return i

    return 1


def is_prime(n):
    """ Returns true if n is prime, else false. """
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


