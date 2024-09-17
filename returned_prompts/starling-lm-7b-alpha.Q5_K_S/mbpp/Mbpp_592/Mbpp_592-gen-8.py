
def sum_Of_product(n):
    return sum(list(map(lambda x: x[0]*x[1], zip(binom(n+1),binom(n+1)[1:]))))

def binom(n):
    return tuple(list(range(n+1))) + tuple(list(range(n))[::-1])


