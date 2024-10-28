def sum_series(n):
    result = 0
    for i in range(0, n // 2 + 1):
        result += n - 2 * i
    return result