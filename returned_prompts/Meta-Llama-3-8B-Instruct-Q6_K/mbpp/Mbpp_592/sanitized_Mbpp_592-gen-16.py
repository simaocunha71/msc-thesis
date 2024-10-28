def sum_Of_product(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        result *= (n-i+1)
    return result