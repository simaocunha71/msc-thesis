def sumofFactors(n: int) -> int:
    factors = []
    for i in range(1,n+1):
        if(n%i==0):
            factors.append(i)
    factors_even = []
    for i in factors:
        if(i%2==0):
            factors_even.append(i)
    return sum(factors_even)