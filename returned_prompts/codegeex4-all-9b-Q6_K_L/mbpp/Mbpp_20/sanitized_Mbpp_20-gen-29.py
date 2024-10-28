def is_woodall(n):
    if n <= 0:
        return False
    sum = 0
    i = 1
    while i <= n:
        if n % i == 0:
            sum += i
        i += 1
    return sum == n * n