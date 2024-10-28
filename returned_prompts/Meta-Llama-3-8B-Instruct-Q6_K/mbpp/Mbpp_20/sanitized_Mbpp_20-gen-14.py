def is_woodall(n):
    i = 1
    while True:
        if 2**(i-1)*2**i - 1 == n:
            return True
        elif 2**(i-1)*2**i - 1 > n:
            return False
        i += 1