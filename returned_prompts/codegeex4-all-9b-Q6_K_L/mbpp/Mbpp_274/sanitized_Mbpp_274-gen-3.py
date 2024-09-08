def even_binomial_Coeff_Sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (2 * even_binomial_Coeff_Sum(n - 1)) - even_binomial_Coeff_Sum(n - 2)