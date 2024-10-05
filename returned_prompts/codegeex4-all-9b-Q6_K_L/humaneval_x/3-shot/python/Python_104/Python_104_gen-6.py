    def is_unique_digit(num):
        digits = set(str(num))
        return all(int(digit) % 2 != 0 for digit in digits)

    return sorted(filter(is_unique_digit, x))

