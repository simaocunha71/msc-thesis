def even_binomial_Coeff_Sum(n):
    even_sum = 0
    for k in range(0, n//2 + 1):
        even_sum += binomial_coefficient(n, k)
    return even_sum
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)