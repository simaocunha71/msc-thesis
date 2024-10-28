def is_woodall(n):
    sum = 0
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum == 2*n