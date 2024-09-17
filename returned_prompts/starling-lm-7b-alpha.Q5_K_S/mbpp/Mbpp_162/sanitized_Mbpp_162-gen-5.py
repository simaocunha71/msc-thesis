def sum_series(n):
    s = 0
    if n % 2 == 0:
        for i in range(n // 2):
            s += n - 2 * i
    else:
        for i in range(n // 2):
            s += n - 2 * i
        s += n
    return s