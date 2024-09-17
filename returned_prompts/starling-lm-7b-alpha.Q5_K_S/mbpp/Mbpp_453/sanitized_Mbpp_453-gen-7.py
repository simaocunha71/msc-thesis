def sumofFactors(n):
    if n < 0:
        return -1
    factors = [i for i in range(1,n + 1) if n % i == 0]
    return