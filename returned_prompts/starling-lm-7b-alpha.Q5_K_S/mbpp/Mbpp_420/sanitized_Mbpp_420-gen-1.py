def cube_Sum(n):
    result = 0
    for i in range(1, n+1, 2):
        result += i**3
    return result