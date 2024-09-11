def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))  # 1,3,5,7...n*2-1