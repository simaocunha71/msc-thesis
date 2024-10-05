    def generate_even_numbers(start, end):
        yield from (2 * i for i in range(start, end + 1, 2))

    def generate_odd_numbers(start, end):
        yield from (2 * i + 1 for i in range(start, end + 1, 2))

    if (b - a) % 2 == 0:
        return list(generate_even_numbers(a, b))
    else:
        return list(generate_odd_numbers(a, b))


