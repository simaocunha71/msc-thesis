def tuple_to_dict(my_tuple):
    if len(my_tuple) == 0 or len(my_tuple) % 2 == 1:
        return None
    result = {}
    for i in range(0, len(my_tuple), 2):
        result[my_tuple[i]] = my_tuple[i + 1]
    return result