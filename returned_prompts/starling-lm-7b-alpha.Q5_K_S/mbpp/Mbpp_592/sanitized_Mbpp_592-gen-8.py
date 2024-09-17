def sum_Of_product(n):
    # calculate binomial coefficient
    def binomial(n, r):
        if r == 0:
            return 1
        else:
            return n * binomial(n-1, r-1) / r
    # calculate sum of product
    summ = 0
    for i in range(n+1):
        summ += binomial(n, i) * binomial(n-1, i)
    return summ