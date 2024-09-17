def is_polite(n):
    if n < 10:
        return n
    if n % 10 == 0 or n % 10 == 1:
        return is_polite(n // 10)
    if n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        return n + 1
    if n % 10 == 5 or n % 10 == 6:
        return is_polite(n - 1)
    if n % 10 == 7 or n % 10 == 8:
        return is_polite(n + 1)
    if n % 10 == 9:
        return is_polite(n - 1)