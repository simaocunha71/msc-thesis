def even_binomial_Coeff_Sum(n):
    if n < 1:
        return 0
    result = 0
    for k in range(n):
        if k % 2 == 0:
            result += binomial_coefficient(n, k)
    return result
def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result