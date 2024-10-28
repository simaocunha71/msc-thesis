def sum_Of_product(n):
    product = 1
    for i in range(n):
        product *= binomial(n-i, i)
    return product
def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)