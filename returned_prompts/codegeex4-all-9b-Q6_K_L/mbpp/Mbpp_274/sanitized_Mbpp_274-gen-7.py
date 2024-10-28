def even_binomial_Coeff_Sum(n):
    total = 0
    for i in range(n+1):
        binom_coeff = math.comb(n, i)
        if i % 2 == 0:
            total += binom_coeff
    return total