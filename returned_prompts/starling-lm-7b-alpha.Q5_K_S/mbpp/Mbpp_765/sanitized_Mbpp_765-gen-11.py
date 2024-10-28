def is_polite(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return is_polite(n-1) + 10