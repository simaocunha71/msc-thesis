from math import comb
def even_binomial_Coeff_Sum(n: int) -> int:
    sum_of_even_binomial_coeff = 0
    for i in range(n):
        if i % 2 == 0:
            sum_of_even_binomial_coeff += comb(n-1, i)
    return sum_of_even_binomial_coeff