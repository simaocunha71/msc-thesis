def sum_series(n):
    total = 0
    while n > 0:
        total += n
        n -= 2
    return total