def tuple_str_int(s):
    s = s[1:-1]
    return tuple(int(i) for i in s.split(','))