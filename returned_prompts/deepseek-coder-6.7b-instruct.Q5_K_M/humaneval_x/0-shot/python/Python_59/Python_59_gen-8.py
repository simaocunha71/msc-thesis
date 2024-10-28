

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#problem_12.py
