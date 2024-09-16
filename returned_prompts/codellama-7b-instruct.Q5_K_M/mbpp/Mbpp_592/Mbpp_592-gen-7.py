def sum_Of_product(n):
    return sum([binomial(n, i) * binomial(n, n - i) for i in range(n)])

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)
