def sum_Of_product(n):
    sum_val = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            sum_val += binom(i, j)
    return sum_val
def binom(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result