    def is_prime(n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    def sum_digits(n):
        return sum(int(digit) for digit in str(n))

    prime = max(filter(is_prime, lst), default=None)
    return sum_digits(prime) if prime is not None else 0

