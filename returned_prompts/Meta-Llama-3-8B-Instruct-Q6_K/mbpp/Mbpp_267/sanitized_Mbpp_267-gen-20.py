def square_Sum(n):
    total = 0
    for i in range(1, 2*n, 2):
        total += i ** 2
    return total