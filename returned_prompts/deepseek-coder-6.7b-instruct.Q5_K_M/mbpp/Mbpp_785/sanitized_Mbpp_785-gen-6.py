def tuple_str_int(tup):
    tup = tup.replace("(", "").replace(")", "")
    tup = tup.split(",")
    tup = tuple(map(int, tup))
    return tup