def even_binomial_Coeff_Sum(n):
    binom_coeff = [1] + [0] * (n - 1)
    for i in range(n):
        for j in range(i + 1, n):
            binom_coeff[j] += binom_coeff[j - 1]
    return sum(binom_coeff[i] for i in range(0, n, 2))