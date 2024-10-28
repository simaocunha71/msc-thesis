def even_binomial_Coeff_Sum(n):
    result = 0
    for k in range(0, n+1):
        if k % 2 == 0:
            result += binomial_coefficient(n, k)
    return result

def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k+1):
        result *= (n-i+1) / i
    return result
