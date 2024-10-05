    for i in range(2, 10):
        if a % i == 0 and is_prime(i) and is_prime(a // i):
            return True
    return False


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


