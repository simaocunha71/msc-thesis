
def cube_Sum(n):
    total = 0
    for i in range(2, 2*n+1, 2):
        total += i**3
    return total


