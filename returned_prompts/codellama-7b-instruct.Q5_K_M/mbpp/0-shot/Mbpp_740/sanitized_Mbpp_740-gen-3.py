def tuple_to_dict(my_tuple):
    return {my_tuple[i]: my_tuple[i+1] for i in range(0, len(my_tuple), 2)}