def tuple_str_int(s):
    t = s[1:-1]
    t = t.replace(', ', ',')
    return tuple(map(int, t.split(',')))