def is_polite(n):
    if n < 1:
        return None
    total = 0
    i = 1
    while total < n:
        total += i
        i += 1
    return total - n