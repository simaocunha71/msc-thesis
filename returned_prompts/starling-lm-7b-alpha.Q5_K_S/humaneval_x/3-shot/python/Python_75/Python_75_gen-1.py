    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    if is_prime(a) and is_prime(a-2) and is_prime(a-3):
        return True
    else:
        return False


