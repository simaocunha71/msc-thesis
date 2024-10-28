def sum_series(n):
    if n < 2:
        return 0
    return sum(n - 2 * i for i in range(n // 2 + 1))