    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = 1
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            largest_prime = i

    return largest_prime


