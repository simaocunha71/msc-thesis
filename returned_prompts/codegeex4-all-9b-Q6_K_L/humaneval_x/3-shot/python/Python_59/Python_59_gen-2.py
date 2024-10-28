    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_factor = None
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor

