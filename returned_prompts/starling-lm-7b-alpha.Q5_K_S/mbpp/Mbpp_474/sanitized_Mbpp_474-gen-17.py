def replace_char(s, old, new):
    return ''.join(new if ch == old else ch for ch in s)