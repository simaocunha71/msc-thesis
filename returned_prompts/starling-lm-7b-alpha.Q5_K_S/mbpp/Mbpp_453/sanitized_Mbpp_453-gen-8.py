def factors(n): 
    a = [] 
    for i in range(1, n + 1): 
        if n % i == 0: 
            a.append(i) 
    return a
def sumofFactors(n):
    sum = 0
    factorlist = factors(n)
    for i in factorlist:
        if(i % 2 == 0):
            sum += i
    return sum