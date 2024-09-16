def extract_even(nested_tuple):
    for i in range(len(nested_tuple)):
        if isinstance(nested_tuple[i], tuple):
            nested_tuple[i] = extract_even(nested_tuple[i])
        else:
            if nested_tuple[i] % 2 != 0:
                nested_tuple.pop(i)
    return nested_tuple