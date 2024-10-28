def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(i):
            if j % 2 == 0:
                sum += binomial_coefficient(i, j)
    return sum
def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    return result