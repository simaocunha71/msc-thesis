def sum_series(n):
    if (n % 2 != 0):
        return (n * (n + 1)) / 2 - (n - 1) / 2
    else:
        return (n * (n + 1)) / 2 - (n) / 2