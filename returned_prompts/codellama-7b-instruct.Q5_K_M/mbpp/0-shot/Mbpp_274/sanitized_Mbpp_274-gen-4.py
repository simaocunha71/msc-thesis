def even_binomial_Coeff_Sum(n):
    return sum([(comb(n, i)) for i in range(0, n) if i % 2 == 0])
def comb(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res