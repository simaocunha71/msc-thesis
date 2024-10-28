
def even_binomial_Coeff_Sum(n):
    return sum(binomial_Coeff(n,i) for i in range(0,n+1,2))


def binomial_Coeff(n, k):
    return (fact(n) / (fact(k) * fact(n - k)))


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


