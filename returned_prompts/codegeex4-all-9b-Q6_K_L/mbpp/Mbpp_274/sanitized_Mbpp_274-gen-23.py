def even_binomial_Coeff_Sum(n: int) -> int:
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += math.comb(n, i)
    return sum