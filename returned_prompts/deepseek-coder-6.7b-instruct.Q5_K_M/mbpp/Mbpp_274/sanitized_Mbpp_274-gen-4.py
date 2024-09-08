def even_binomial_Coeff_Sum(n):
    res = 0
    for i in range(0, n + 1, 2):
        res += binom(n, i)
    return res