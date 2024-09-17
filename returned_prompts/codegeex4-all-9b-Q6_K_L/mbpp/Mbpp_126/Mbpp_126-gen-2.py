def sum(a, b):
    if a > b:
        a, b = b, a
    sum = 0
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            sum += i
    return sum

