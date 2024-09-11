def square_Sum(n):
    return sum([i**2 for i in range(2, 2*n, 2)])  # or sum(i**2 for i in range(2, 2*n, 2)) in python 3.x