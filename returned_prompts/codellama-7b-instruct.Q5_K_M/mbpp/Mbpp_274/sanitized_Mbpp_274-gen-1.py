def even_binomial_Coeff_Sum(n):
    return sum(binomial_coefficient(n, i) for i in range(0, n+1, 2))
def binomial_coefficient(n, k):
    if k > n // 2:
        k = n - k
    res = 1
    for i in range(k+1):
        res *= n-i
        res //= i+1
    return res