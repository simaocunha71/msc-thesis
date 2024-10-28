    for i in range(1, 10):
        if a % i == 0 and is_prime(i):
            a //= i
        else:
            return False
    return True

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


