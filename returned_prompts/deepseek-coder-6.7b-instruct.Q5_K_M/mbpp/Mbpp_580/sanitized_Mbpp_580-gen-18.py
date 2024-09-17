def extract_even(tup):
    result = []
    for item in tup:
        if isinstance(item, tuple):
            new_tuple = extract_even(item)
            if new_tuple:
                result.append(new_tuple)
        elif item % 2 == 0:
            result.append(item)
    return tuple(result)