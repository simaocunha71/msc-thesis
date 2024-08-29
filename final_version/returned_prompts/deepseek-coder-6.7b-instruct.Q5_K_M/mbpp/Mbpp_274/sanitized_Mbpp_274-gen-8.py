def even_binomial_Coeff_Sum(n):
    def binomial_coeff(n, k):
        res = 1
        if (k > n - k):
            k = n - k
        for i in range(0 , k):
            res = res * (n - i)
            res = res // (i + 1)
        return res

    sum = 0
    for i in range(0, n + 1, 2):
        sum += binomial_coeff(n, i)

    return sum