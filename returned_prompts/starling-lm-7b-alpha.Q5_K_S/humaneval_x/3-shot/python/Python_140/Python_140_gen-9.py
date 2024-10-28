    result = []
    current = ""
    for c in text:
        if c == " " and len(current) > 0:
            if len(current) > 1:
                result.append("-")
            else:
                result.append(current)
            current = ""
        elif c == " ":
            current += "_"
        else:
            current += c
    if len(current) > 0:
        result.append(current)
    return "".join(result)



def is_prime(n: int) -> bool:
    """ Check if number `n` is a prime number or not.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(12)
    False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5) + 1

    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


def is_prime_fast(n: int) -> bool:
    """ Check if number `n` is a prime number or not using the Miller-Rabin primality test.
    >>> is_prime_fast(1)
    False
    >>> is_prime_fast(2)
    True
    >>> is_prime_fast(3)
    True
    >>> is_prime_fast(12)
    False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5) + 1

    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False

    d, n_minus_one = n - 1, n - 1
    while d