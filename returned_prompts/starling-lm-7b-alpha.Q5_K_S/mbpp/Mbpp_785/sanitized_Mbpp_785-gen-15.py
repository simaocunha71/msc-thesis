def tuple_str_int(s):
    s = s.replace("(","").replace(")","").replace(",","")
    return tuple(map(int, s.split()))