def even_binomial_Coeff_Sum(n):
    def binomial_Coeff(k, n):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return binomial_Coeff(k - 1, n - 1) + binomial_Coeff(k, n - 1)
    return sum(binomial_Coeff(k, n) for k in range(0, n + 1, 2))