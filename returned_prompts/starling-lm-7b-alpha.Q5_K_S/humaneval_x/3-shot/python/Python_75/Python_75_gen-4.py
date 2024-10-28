    def is_prime(a):
        if a < 2:
            return False
        for n in range(2, int(a**0.5) + 1):
            if a % n == 0:
                return False
        return True

    for i in range(3, a):
        if is_prime(i) and is_prime(a // i):
            return True

    return False


