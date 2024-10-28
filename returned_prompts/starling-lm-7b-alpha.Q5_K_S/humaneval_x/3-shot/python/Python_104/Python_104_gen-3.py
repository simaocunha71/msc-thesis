    def has_even_digit(n):
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False

    def has_odd_digit(n):
        for digit in str(n):
            if int(digit) % 2 == 0:
                return False
        return True

    return sorted([i for i in x if has_odd_digit(i)])


