def count_divisors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            count += 1
    if n > 1:
        count += 1
    return count % 2 == 0