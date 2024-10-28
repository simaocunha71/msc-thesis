def is_woodall(n):
    i = 1
    while True:
        if (i**2) * 2**i + 1 == n:
            return True
        elif (i**2) * 2**i + 1 > n:
            return False
        i += 1