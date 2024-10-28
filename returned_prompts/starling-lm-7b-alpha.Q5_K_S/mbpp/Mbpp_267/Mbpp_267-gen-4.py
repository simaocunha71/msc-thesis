
def square_Sum(n):
    if n == 0:
        return 0
    else:
        return (2*n)**2 + square_Sum(n-1)


