def even_binomial_Coeff_Sum(n):
    assert(n>=1)
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += 1
    return sum