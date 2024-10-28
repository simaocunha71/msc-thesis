    def has_even_digits(n):
        return any(d % 2 == 0 for d in str(n))

    def has_only_odd_digits(n):
        return all(d % 2 == 1 for d in str(n))

    return sorted([i for i in x if has_only_odd_digits(i)])


