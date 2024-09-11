def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for i in range(n):
        total_sum += binomial_coefficient(i, n) if i % 2 == 0 else 0
    return total_sum
def binomial_coefficient(k, n):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result