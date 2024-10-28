def square_Sum(n):
    result = 0
    for i in range(1, 2 * n + 1, 2):
        result += i ** 2
    return result