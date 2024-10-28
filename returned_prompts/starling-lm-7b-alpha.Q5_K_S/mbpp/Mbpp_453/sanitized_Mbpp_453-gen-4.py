def sumofFactors(num):
    res = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            if (i % 2 == 0):
                res += i
    return res