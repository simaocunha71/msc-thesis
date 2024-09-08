def sum_series(n):
    total = 0
    for i in range(0, n//2+1):
        total += n - 2*i
    return total