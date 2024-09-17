import math
def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        B = [0]*(n+1)
        B[0] = 1
        B[1] = 1
        for i in range(2, n+1):
            B[i] = sum(binom(i, k)*B[i-k-1] for k in range(i))
        return B[n]
def binom(n, k):
    if k > n-k:
        k = n-k
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) // i
    return result