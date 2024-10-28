def tuple_str_int(s):
    s = s.strip('()')
    s = map(int, s.split(','))
    return tuple(s)