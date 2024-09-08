import ast
def tuple_str_int(tup_str):
    tup_str = tup_str.replace("(", "").replace(")", "").split(",")
    tup_str = tuple(map(int, tup_str))
    return tup_str