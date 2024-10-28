def cube_Sum(n):
    total_sum = 0
    for i in range(2, 2*n+1, 2):
        total_sum += i**3
    return total_sum