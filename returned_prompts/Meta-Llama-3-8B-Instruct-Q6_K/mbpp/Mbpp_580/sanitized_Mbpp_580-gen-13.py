def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(tuple(filter(lambda x: x % 2 == 0, element)))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)