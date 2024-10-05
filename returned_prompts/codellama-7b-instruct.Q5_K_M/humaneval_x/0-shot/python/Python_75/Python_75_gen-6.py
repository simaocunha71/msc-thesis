
    if a < 100:
        return False
    for i in range(2, 10):
        if a % i == 0:
            if is_prime(i) and is_prime(a // i) and is_prime(a // (a // i)):
                return True
    return False

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True