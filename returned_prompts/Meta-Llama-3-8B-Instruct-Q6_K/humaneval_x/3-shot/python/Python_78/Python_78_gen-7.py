    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D', 'F']
    count = 0
    for digit in num:
        if digit in prime_hex_digits:
            count += 1
    return count
    # return sum(1 for digit in num if digit in prime_hex_digits)  # Use a generator expression


