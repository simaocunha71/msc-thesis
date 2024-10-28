def is_woodall(n):
    if n < 2:
        return False
    sum = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum += i + n // i
            else:
                sum += i
            i += 1
    return sum == n