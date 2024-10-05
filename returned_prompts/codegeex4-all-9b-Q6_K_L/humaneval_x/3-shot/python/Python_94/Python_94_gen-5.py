    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = max(filter(is_prime, lst), default=None)
    if max_prime is None:
        return 0
    return sum(map(int, str(max_prime)))


