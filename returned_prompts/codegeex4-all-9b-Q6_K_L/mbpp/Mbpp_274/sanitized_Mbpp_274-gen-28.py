def even_binomial_Coeff_Sum(n):
    result = 0
    for i in range(n+1):
        coeff = math.comb(n, i)
        if i % 2 == 0:
            result += coeff
    return result