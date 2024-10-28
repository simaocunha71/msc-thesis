def sum_series(n):
    result = 0
    for i in range(n // 2 + 1):
        result += n - 2 * i
    return result