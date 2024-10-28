def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(0,n+1):
        if i % 2 == 0:
            sum += binomial_Coeff(n,i)
    return sum

def binomial_Coeff(n,r):
    if r == 0 or r == n:
        return 1
    return binomial_Coeff(n-1,r-1) + binomial_Coeff(n-1,r)