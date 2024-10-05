    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = None
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime

