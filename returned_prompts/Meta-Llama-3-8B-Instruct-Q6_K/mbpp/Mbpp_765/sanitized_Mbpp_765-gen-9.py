def is_polite(n):
    if n < 1:
        return -1
    total = 0
    i = 1
    while True:
        total += i
        i += 1
        if total >= n:
            return total - n
        if total > n:
            return -1
    return -1