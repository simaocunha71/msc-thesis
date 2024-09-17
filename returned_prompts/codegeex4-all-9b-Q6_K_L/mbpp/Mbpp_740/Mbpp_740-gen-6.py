def tuple_to_dict(tup: tuple):
    return dict(zip(tup[::2], tup[1::2]))