def sum_average(n):
    total = 0
    for i in range(1, n+1):
        total += i
    average = total / n
    return total, average