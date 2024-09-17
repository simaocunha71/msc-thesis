
def extract_even(nested_tup):
    even_tup = []
    for elem in nested_tup:
        if isinstance(elem, tuple):
            even_tup.append(extract_even(elem))
        elif elem % 2 == 0:
            even_tup.append(elem)
    return tuple(even_tup)


