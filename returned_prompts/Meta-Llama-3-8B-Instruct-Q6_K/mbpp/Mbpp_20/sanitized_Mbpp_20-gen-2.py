def is_woodall(n):
    if n < 1:
        return False
    sum = 0
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum == n - 1