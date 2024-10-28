def is_polite(n):
    if n < 10:
        return n
    if n % 100 == 0:
        return 0
    if n % 10 == 0 or n % 10 == n // 10:
        return is_polite(n // 10)
    return 0