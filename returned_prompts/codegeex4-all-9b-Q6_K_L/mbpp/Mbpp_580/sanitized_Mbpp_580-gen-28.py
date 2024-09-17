def extract_even(mixed_tuple):
    even_tuple = tuple(i for i in mixed_tuple if isinstance(i, int) and i % 2 == 0)
    return even_tuple