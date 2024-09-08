def sumofFactors(num):
    sum = 0
    for i in range(1, num+1):
        if num % i == 0 and i % 2 == 0:
            sum += i
    return sum