
    a, b = 1, 2
    for _ in range(n):
        a, b = b, a + b
        while not is_prime(a):
            a += 1
    return a


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
