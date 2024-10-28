def catalan_number(n):
    return sum([binom(2*i, i) for i in range(n+1)])
def binom(n,k):
    if k>n//2:
        k=n-k
    res=1
    for i in range(k+1):
        res*=n-i
        res//=i+1
    return res