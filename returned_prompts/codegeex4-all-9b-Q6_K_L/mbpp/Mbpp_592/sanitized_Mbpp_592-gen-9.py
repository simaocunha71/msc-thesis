def sum_Of_product(n):
    product_sum = 0
    for i in range(n):
        product_sum += binomial(n, i) * binomial(n, i + 1)
    return product_sum
def binomial(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)