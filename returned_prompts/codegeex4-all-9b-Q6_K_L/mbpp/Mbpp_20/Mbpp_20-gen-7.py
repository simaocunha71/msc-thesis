def is_woodall(n):
    i = 2
    sum = 0
    while n > 0:
        sum += i * (n % 10)
        n //= 10
        i += 1
    return sum == 383

