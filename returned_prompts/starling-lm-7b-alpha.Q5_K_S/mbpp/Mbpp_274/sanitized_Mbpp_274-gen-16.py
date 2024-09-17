from math import factorial
def binomial_coeff(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))
def even_binomial_Coeff_Sum(n: int) -> int:
    s = 0
    for i in range(0, n + 1, 2):
        s += binomial_coeff(n, i)
    return s