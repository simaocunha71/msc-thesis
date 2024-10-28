def sum_series(n):
    assert isinstance(n, int), 'n must be an integer'
    assert n > 0, 'n must be a positive integer'
    if n % 2 == 0:
        return n * (n // 2) + (n + 2) // 4
    else:
        return n * (n // 2) + (n + 1) // 2