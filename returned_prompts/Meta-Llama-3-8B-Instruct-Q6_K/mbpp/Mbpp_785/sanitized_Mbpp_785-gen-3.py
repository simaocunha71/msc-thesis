def tuple_str_int(s):
    return eval(s) if s.startswith('(') and s.endswith(')') else tuple(map(int, s[1:-1].split(','))) if s[1:-1].replace(',', '').isdigit() else None