    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            largest_factor = max(largest_factor, i)
    return largest_factor

