def cube_Sum(n: int) -> int:
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**3
    return sum