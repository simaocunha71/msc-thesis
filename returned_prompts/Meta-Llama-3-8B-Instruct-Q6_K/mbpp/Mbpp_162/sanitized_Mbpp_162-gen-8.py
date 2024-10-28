def sum_series(n):
    return sum(i for i in range(n//2 + 1) if i <= n//2) * 2 - n