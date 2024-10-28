def sum_Of_product(n):
    if n <= 0:
        return 0
    result = 0
    for i in range(1, n + 1):
        result += i * binomial_coefficient(i, n)
    return result
def binomial_coefficient(k, n):
    if k > n:
        return 0
    if k > n // 2:
        return binomial_coefficient(n - k, n)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result