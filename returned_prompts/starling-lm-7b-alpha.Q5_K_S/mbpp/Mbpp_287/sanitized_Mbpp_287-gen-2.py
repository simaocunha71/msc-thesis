def square_Sum(n):
    result = 0
    for i in range(2, 2*n+1, 2):
        result += i*i
    return result