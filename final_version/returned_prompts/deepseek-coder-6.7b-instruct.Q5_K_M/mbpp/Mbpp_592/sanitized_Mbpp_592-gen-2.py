def binomial(n):
    return n * (n-1) // 2
def sum_Of_product(n):
    sum_ = 0
    for i in range(1, n):
        sum_ += binomial(i) * binomial(i+1)
    return sum_