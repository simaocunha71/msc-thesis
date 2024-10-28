def even_binomial_Coeff_Sum(n):
    result = 0
    for k in range(n):
        if k % 2 == 0:
            result += binomial_coeff(n, k)
    return result
def binomial_coeff(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result