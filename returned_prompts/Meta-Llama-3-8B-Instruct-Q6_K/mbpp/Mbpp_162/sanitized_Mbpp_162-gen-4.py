def sum_series(n):
    return sum(range(0, n//2 + 1, 2)) * 2 + n if n % 2 else sum(range(0, n//2, 2)) * 2