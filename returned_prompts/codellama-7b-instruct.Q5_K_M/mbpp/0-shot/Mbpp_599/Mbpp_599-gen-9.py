def sum_average(n):
    sum = 0
    for i in range(n):
        sum += i + 1
    average = sum / n
    return (sum, average)