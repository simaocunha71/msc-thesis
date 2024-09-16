def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += binomialCoeff(n, i)
    return sum

def binomialCoeff(n, k):
    if k < 0 or n < k:
        return 0
    if k == 0 or k == n:
        return 1
    return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)
