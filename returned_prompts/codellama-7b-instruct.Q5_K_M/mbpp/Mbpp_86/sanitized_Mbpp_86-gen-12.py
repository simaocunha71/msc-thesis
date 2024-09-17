def centered_hexagonal_number(n):
    return int(((1 + 2 * (n // 2)) ** 2) / 2 + n % 2)