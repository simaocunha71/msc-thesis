def is_woodall(n):
    i = 1
    while True:
        woodall = i * (2**i) + 1
        if woodall == n:
            return True
        if woodall > n:
            return False
        i += 1