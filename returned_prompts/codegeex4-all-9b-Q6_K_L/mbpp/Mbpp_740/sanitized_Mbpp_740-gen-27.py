def tuple_to_dict(tup):
    if len(tup) % 2 != 0:
        raise ValueError("Input tuple must have an even length.")
    return dict(zip(tup[::2], tup[1::2]))