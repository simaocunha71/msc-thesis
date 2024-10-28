def even_binomial_Coeff_Sum(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += binomial_coefficient(n, i)
    return result
def binomial_coefficient(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result