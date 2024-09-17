
def sum_series(n):
    s = 0
    for i in range(n // 2):
        s += n - 2 * i
    return s


