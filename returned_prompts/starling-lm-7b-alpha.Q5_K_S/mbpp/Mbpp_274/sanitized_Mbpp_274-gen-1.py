def even_binomial_Coeff_Sum(n):
    binomialCoeff = [1]
    for i in range(1,n+1):
        binomialCoeff.append(sum(binomialCoeff[-i:]))
    return sum(binomialCoeff[::2])