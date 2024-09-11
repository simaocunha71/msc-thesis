def eulerian_num(n, m):
    result = 0
    for i in range(m):
        result += binomial_coefficient(n, i) * eulerian_num(n - i, m - 1)
    return result
def binomial_coefficient(n, k):
    if k > n // 2:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result