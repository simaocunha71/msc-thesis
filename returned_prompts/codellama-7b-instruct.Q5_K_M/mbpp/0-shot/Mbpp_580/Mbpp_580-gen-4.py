def extract_even(nested_mixed_tuple):
    result = []
    for element in nested_mixed_tuple:
        if isinstance(element, int) and element % 2 == 0:
            result.append(element)
        elif isinstance(element, tuple):
            result.append(extract_even(element))
    return tuple(result)
