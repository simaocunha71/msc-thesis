def is_undulating(n):
    while n > 0:
        d = n % 10
        if d != (n % 100) / 10:
            return False
        n //= 10
    return True