def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0 and n % i == 0:
            sum = sum + i
    return sum