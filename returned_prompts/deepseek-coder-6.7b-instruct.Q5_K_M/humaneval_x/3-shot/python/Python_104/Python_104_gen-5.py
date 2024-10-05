    def has_even_digit(num):
        return any(int(d) % 2 == 0 for d in str(num))

    return sorted([num for num in x if not has_even_digit(num)])


