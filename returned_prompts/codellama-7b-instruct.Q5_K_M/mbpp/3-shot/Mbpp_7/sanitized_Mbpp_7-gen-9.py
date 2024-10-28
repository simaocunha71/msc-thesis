def find_char_long(str_in):
    words = str_in.split()
    return [w for w in words if len(w) >= 4]