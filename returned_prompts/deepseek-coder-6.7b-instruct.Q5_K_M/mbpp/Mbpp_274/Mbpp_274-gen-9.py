
def even_binomial_Coeff_Sum(n):
    bc = [0]*(n+1)
    bc[0] = 1
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            bc[j] = bc[j] + bc[j-1]
    return sum(bc[i] for i in range(0, n+1, 2))


