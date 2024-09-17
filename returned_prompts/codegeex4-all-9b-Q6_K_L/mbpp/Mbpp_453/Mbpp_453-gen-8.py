def sumofFactors(n):
    sum = 0
    for i in range(2, n):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum

