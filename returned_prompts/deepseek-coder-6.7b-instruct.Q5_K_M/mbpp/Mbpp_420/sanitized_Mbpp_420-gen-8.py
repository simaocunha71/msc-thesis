def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        num = 2 * i
        sum += num ** 3
    return sum