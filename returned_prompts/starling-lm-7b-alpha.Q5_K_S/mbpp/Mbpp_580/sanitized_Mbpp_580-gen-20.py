def extract_even(test_tup):
    new_tuple = []
    for item in test_tup:
        if isinstance(item, tuple):
            new_tuple.append(extract_even(item))
        elif item % 2 == 0:
            new_tuple.append(item)
    return tuple(new_tuple)