def extract_even(nested_tuple):
    def is_even(element):
        if isinstance(element, tuple):
            return extract_even(element)
        else:
            return element % 2 == 0

    return tuple(filter(is_even, nested_tuple))