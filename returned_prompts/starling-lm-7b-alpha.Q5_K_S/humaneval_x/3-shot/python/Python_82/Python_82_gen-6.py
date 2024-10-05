    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if len(string) % 2 == 0:
        return False
    else:
        for i in range(3, len(string) + 1, 2):
            if is_prime(i):
                return True
        return False


