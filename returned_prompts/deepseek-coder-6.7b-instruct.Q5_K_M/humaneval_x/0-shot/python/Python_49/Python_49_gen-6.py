
    result = 1
    while n:
        if n & 1:
            result = (result * 2) % p
        n >>= 1
        if result > p:
            result -= p
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


