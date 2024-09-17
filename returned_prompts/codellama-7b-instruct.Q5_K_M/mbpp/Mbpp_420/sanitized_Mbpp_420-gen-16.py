def cube_Sum(n: int) -> int:
    total = 0
    for i in range(2, n+1):
        total += i**3
    return total