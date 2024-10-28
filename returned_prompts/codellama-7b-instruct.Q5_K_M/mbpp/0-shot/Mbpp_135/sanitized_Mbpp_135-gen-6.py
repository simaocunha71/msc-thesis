def hexagonal_num(n):
    if n == 1:
        return 1
    else:
        return triangular_num(n) - triangular_num(n-1)
def triangular_num(n):
    return n*(n+1)/2