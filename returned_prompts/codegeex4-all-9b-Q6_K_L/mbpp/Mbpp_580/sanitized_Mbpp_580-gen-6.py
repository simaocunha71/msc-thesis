def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)