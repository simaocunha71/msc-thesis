def sum_Of_product(n):
    result = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            result += binom(i, j)
    return result
def binom(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) / i
    return int(result)