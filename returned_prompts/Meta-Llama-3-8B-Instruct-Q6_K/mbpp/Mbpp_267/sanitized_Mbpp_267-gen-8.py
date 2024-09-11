def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2)) if n > 0 else 0