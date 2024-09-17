def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for k in range(n):
        if k % 2 == 0:
            total_sum += binomial_coefficient(k, n)
    return total_sum
def binomial_coefficient(k, n):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result