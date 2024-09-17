def sum_Of_product(n):
    sum = 0
    for i in range(0, n):
        sum += binomial_coeff(n, i) * binomial_coeff(n, n - i - 1)
    return sum
def binomial_coeff(n, k):
    if k < 0 or n < k:
        return 0
    if k == 0 or n == k:
        return 1
    return binomial_coeff(n - 1, k - 1) + binomial_coeff(n - 1, k)