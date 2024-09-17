import math
def binomial(n):
    return math.comb(n, n)
def sum_Of_product(n):
    sum = 0
    for i in range(n):
        sum += binomial(i) * binomial(n - i - 1)
    return sum