def sum_Of_product(n):
    sum_of_product = 0
    for i in range(n+1):
        for j in range(i+1):
            sum_of_product += binomial_coefficient(n, i) * binomial_coefficient(n, j)
    return sum_of_product
def binomial_coefficient(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result