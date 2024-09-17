def is_woodall(n):
    if n <= 0:
        return False
    while n > 1:
        d = n % 10
        if d == 0 or n % d != 0:
            return False
        n //= 10
    return True