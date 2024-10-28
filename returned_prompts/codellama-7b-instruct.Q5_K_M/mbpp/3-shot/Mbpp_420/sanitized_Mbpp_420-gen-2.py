def cube_Sum(n):
    sum = 0
    for i in range(2, n + 1):
        sum += i ** 3
    return sum