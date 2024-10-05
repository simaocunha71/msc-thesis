    def has_even_digit(n):
        return any(int(digit) % 2 == 0 for digit in str(n))

    return sorted([x for x in x if not has_even_digit(x)])  # using list comprehension and has_even_digit function


