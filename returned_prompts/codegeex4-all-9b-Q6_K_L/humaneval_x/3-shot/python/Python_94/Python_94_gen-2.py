    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_digits(n):
        return sum(int(digit) for digit in str(n))

    max_prime = max(filter(is_prime, lst))
    return sum_digits(max_prime)

