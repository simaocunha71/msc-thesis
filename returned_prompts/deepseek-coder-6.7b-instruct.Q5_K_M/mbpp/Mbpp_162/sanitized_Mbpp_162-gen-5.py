def sum_series(n):
    sum = 0
    i = 0
    while n - 2 * i >= 0:
        sum += n - 2 * i
        i += 1
    return sum