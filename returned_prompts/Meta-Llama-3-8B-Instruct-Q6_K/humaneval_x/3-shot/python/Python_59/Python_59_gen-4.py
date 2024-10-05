    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factor = 2
    while n % factor != 0:
        factor += 1
    largest_factor = factor
    while n % factor == 0:
        largest_factor = factor
        n /= factor
        while n % factor == 0:
            n /= factor
    return largest_factor


