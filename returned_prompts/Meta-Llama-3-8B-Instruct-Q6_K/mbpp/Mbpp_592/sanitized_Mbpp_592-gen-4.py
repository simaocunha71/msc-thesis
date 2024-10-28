def sum_Of_product(n):
    result = 0
    for i in range(n+1):
        for j in range(i+1):
            result += (binomial(n, i) * binomial(n, j))
    return result
def binomial(n, k):
    if k > n//2:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result