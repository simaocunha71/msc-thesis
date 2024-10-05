    count = 0

    for hex_digit in num:
        if is_prime(int(hex_digit, 16)):
            count += 1

    return count


def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


