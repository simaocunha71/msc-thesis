def is_woodall(n):
    for i in range(1, int(n**0.5) + 1):
        if 2**i * 3**(i-1) + 1 == n:
            return True
    return False