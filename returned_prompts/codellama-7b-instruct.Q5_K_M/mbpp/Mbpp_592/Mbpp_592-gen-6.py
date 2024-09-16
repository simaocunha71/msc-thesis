"""
def sum_Of_product(n):
    s = 0
    for i in range(0,n):
        s += binomial_coefficient(n,i) * binomial_coefficient(n,n-i-1)
    return s

def binomial_coefficient(n,k):
    if k<0 or n<k:
        return 0
    if k==0 or k==n:
        return 1
    return binomial_coefficient(n-1,k-1) + binomial_coefficient(n-1,k)
"""
