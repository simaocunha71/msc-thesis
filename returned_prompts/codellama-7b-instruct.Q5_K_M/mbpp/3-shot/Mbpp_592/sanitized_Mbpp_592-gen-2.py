def sum_Of_product(n):
    sum = 0
    for i in range(n):
        sum += binomial_coefficient(i+1, i+1)
    return sum
def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res