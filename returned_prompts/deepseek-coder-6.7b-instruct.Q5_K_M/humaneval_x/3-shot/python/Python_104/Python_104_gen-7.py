    def has_even_digit(n):
        return any(int(d) % 2 == 0 for d in str(n))

    return sorted([n for n in x if not has_even_digit(n)])


