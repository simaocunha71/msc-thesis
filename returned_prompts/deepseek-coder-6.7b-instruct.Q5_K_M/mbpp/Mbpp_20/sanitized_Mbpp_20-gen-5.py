def is_woodall(n):
    if n > 0:
        while n % 2 == 0:
            n = n // 2
        return n == 1
    else:
        return False