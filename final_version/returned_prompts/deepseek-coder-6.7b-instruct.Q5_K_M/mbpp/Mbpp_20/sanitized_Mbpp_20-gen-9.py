def is_woodall(n):
    if n < 2:
        return False
    while n % 2 == 0:
        n /= 2
    return all(n % i and n % (i + 2) for i in range(3, int(n ** 0.5) + 1, 6))