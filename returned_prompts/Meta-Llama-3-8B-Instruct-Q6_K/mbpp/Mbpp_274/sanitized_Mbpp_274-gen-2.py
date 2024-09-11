def even_binomial_Coeff_Sum(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += binomial_coefficient(i, n)
    return total
def binomial_coefficient(k, n):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result