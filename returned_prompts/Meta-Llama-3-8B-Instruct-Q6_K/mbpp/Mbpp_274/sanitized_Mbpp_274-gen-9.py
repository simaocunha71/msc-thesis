import math
def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for k in range(n):
        if k % 2 == 0:
            total_sum += binomial(n, k)
    return total_sum
def binomial(n, k):
    return math.comb(n, k)  # or math.factorial(n) // (math.factorial(k) * math.factorial(n-k)) for Python 3.8 and below