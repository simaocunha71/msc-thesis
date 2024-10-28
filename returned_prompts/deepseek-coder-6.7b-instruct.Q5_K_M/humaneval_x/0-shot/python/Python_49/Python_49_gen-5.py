

    # Calculation of 2^n modulo p
    result = 1
    while n > 0:
        if n % 2 != 0:
            result = (result * 2) % p
        n = n // 2
        if result >= p:
            result -= p
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()


