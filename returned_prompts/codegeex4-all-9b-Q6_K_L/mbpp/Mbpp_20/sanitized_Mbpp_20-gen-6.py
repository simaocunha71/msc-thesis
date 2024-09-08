def is_woodall(n):
    p = 1
    while True:
        if p * 2**p - 1 == n:
            return True
        elif p * 2**p - 1 > n:
            return False
        p += 1