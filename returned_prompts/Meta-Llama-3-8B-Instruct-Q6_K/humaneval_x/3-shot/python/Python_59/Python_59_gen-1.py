    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i):
                largest_factor = i
    return largest_factor


