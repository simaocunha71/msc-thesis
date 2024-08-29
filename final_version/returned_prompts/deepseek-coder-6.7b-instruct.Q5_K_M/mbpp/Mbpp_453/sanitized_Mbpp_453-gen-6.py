import math
def sumofFactors(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
            if (n/i) % 2 == 0:
                sum += n//i
    return sum