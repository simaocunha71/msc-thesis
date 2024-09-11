def is_woodall(n):
    if n < 2:
        return False
    sum = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            sum += i
            n //= i
    return sum == n - 1