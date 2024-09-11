def count_divisors(n):
    if n == 0:
        return 0
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False