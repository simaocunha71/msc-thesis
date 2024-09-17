def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += binomial(i, i//2)
    return sum