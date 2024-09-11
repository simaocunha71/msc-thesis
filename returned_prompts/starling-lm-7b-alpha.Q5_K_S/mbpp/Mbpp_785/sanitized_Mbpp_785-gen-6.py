def tuple_str_int(tuple_str):
    tuple_str = tuple_str.replace("(", "").replace(")", "").split(",")
    return tuple(int(i) for i in tuple_str)