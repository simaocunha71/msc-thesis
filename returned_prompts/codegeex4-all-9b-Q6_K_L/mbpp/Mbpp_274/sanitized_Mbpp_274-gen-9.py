def even_binomial_Coeff_Sum(n):
    from math import comb
    total = 0
    for i in range(n+1):
        if i % 2 == 0:
            total += comb(n, i)
    return total