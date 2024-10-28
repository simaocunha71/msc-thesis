def even_Power_Sum(n):
    result = 0
    for i in range(2, n * 2, 2):
        result += i ** 5
    return result