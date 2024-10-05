    def has_even_digit(n):
        for digit in str(n):
            if int(digit) % 2 == 0:
                return True
        return False

    return sorted([x for x in x if not has_even_digit(x)])


