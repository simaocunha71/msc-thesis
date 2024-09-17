from math import comb
def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for i in range(0, n+1, 2):
        total_sum += comb(n, i)
    return total_sum