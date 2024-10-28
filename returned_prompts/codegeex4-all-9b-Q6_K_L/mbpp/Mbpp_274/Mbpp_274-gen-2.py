def even_binomial_Coeff_Sum(n: int) -> int:
    return sum([math.comb(n, i) for i in range(n+1) if i%2==0])