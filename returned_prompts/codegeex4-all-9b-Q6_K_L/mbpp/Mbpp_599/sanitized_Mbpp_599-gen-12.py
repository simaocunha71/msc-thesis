def sum_average(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    average = sum / n
    return sum, average