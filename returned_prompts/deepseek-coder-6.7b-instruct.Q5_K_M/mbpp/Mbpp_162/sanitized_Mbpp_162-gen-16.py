def sum_series(n):
    sum = 0
    for i in range(n//2+1):
        sum += n - 2*i
    return sum