import math
def even_binomial_Coeff_Sum(n):
    total = 0
    for k in range(n + 1):
        if k % 2 == 0:
            total += math.comb(n, k)
    return total