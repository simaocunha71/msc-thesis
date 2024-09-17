
def count_binary_seq(n: int) -> float:
    return binomial_coefficient(2*n, n)

def binomial_coefficient(n: int, k: int) -> float:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)


