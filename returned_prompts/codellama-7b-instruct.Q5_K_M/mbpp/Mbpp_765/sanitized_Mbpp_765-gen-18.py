def is_polite(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 1
    else:
        return n + 2