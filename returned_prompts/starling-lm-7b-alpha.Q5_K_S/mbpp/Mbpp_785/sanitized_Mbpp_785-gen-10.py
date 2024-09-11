def tuple_str_int(tup_str):
    tup = tup_str.strip("()").split(',')
    return tuple(map(int, tup))