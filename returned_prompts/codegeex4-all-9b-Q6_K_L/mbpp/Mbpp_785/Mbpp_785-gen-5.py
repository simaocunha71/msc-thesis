def tuple_str_int(s):
    t = tuple(map(int, s.strip("()").split(", ")))
    return t

