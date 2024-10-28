def cube_Sum(n):
    total = 0
    for i in range(0, 2*n, 2):
        total += i**3
    return total