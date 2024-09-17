def cube_Sum(n):
    if n <= 0:
        return 0
    sum = 0
    for i in range(2, n*2, 2):
        sum += i**3
    return sum