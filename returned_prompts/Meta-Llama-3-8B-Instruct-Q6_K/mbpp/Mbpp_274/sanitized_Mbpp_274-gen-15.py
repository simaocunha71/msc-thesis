def even_binomial_Coeff_Sum(n):
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += binomial_coefficient(n, i)
    return total
def binomial_coefficient(n, k):
    if k > n or k < 0:
        raise ValueError("k must be between 0 and n.")
    if k > n // 2:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result