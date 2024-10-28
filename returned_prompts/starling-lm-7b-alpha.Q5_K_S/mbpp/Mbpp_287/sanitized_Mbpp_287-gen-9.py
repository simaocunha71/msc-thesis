def square_Sum(n):
    if n == 1:
        return 4
    else:
        return (n*n+square_Sum(n-1))