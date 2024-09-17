def extract_even(mixed_tuple):
    result = []
    for item in mixed_tuple:
        if isinstance(item, tuple):
            result.append(extract_even(item))
        elif not item % 2:
            result.append(item)
    return tuple(result)