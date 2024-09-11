def square_Sum(n):
    return sum(i**2 for i in range(2, 2*n+2, 2))  # 2*n+2 is used to include n*n in the range