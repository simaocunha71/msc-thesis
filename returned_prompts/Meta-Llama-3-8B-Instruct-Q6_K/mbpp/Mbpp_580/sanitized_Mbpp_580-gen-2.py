def extract_even(tup):
    result = []
    for element in tup:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result) if result else tuple()  # Convert list to tuple if it's not empty, otherwise return an empty tuple.