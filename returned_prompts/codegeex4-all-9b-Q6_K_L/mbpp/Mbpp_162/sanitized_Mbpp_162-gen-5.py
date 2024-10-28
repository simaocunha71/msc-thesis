def sum_series(n):
    total = 0
    i = 0
    while i <= n // 2:
        total += n - 2 * i
        i += 1
    return total