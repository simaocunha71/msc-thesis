def sumofFactors(n):
    i = 1
    sum = 0
    while i <= math.sqrt(n):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
        i += 1
    return sum

