
def square_Sum(n):
    sum_of_squares = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            sum_of_squares += i**2
    return sum_of_squares


