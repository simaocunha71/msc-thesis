import math
def even_binomial_Coeff_Sum(n):
    sum_even_index_binomial_coeff = 0
    for i in range(n):
        for j in range(i + 1):
            if (i - j) % 2 == 0:
                sum_even_index_binomial_coeff += math.comb(i, j)
    return sum_even_index_binomial_coeff