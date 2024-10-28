def sum_Of_product(n):
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
    
    total_sum = 0
    for i in range(n):
        total_sum += binomial_coefficient(n, i) * binomial_coefficient(n, i + 1)
    return total_sum