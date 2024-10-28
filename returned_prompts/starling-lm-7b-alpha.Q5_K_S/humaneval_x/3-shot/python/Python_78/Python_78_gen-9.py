    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                return False
        return True

    def hex_to_decimal(hex_digit: str) -> int:
        if hex_digit.isdigit():
            return int(hex_digit)
        else:
            return ord(hex_digit) - ord('A') + 10

    count = 0
    for d in num:
        if is_prime(hex_to_decimal(d)):
            count += 1

    return count


