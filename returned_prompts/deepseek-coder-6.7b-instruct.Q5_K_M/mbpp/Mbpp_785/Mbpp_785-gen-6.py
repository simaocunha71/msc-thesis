
def tuple_str_int(tup_str):
    tup_str = tup_str.replace("(", "").replace(")", "")
    tup_int = tuple(map(int, tup_str.split(", ")))
    return tup_int


