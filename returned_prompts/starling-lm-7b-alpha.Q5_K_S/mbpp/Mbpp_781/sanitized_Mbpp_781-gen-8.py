def count_divisors(n):
    count = 0
    i = 1
    while i <= n:
        if (n % i == 0):
            count += 1
        i += 1
    if count % 2 == 0:
        return True
    else:
        return False