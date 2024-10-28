
def modp(n, p):
    n = 2**n
    p = p-1
    while n > p:
        n = n % p
    return n
