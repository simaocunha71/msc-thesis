def even_binomial_Coeff_Sum(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += binomial_coefficient(n, i)
    return total
def binomial_coefficient(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result