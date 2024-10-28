    def is_prime(n):
        if n == 2:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    prime_digits = {
        '2': 2, '3': 3, '5': 5, '7': 7, 'B': 11, 'D': 13, 'E': 17, 'F': 19
    }

    count = 0
    for c in num:
        if c in prime_digits:
            count += prime_digits[c]

    return count


