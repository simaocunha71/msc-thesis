def count_divisors(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c % 2 == 0:
        return True
    else:
        return False