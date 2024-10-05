    def has_even_digit(num):
        while num > 0:
            digit = num % 10
            if digit % 2 == 0:
                return True
            num //= 10
        return False

    return sorted([x for x in x if not has_even_digit(x)])