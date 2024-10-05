    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = -1
    while n % 2 == 0:
        largest_prime = 2
        n >>= 1

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i
    if n > 2:
        largest_prime = n

    return largest_prime


