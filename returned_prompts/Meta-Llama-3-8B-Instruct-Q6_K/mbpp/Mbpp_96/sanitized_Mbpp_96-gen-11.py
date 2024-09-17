def divisor(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * i != n:
                count += 2
            else:
                count += 1
            n //= i
    if n > 1:
        count += 1
    return count