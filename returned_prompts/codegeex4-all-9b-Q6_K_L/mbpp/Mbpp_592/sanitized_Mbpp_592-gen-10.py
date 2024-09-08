def sum_Of_product(n):
    res = 0
    for i in range(1, n):
        res += i * binomial_coefficient(n, i)
    return res
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)