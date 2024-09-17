
def even_binomial_Coeff_Sum(n: int) -> int:
    return sum(binomial_coefficient(n, i) for i in range(0, n+1) if i % 2 == 0)

def binomial_coefficient(n: int, k: int) -> int:
    if k < 0 or n < k:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


