def binomial_product(n):
    product = 1
    for i in range(n):
        product *= (n-i)*(n-i-1)//(i+1)
    return product
def sum_Of_product(n):
    return sum(binomial_product(i) for i in range(1,n+1))