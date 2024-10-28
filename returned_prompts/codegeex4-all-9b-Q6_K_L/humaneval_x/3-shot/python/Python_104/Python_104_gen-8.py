    def has_even_digit(n):
        while n > 0:
            if n % 2 == 0:
                return True
            n //= 10
        return False

    return sorted([x for x in x if not has_even_digit(x)])

