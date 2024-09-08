def cube_Sum(n):
    sum = 0
    num = 2
    for i in range(n):
        sum += num ** 3
        num += 2
    return sum