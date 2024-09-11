def square_Sum(n):
    sum_of_squares = 0
    for i in range(2, 2*n, 2):
        sum_of_squares += i ** 2
    return sum_of_squares