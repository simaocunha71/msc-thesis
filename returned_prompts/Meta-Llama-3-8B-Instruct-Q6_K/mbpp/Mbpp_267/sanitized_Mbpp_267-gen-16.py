def square_Sum(n):
    total_sum = 0
    for i in range(1, 2*n, 2):
        total_sum += i ** 2
    return total_sum