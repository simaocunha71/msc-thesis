def is_decimal(s):
    if '.' in s:
        if len(s.split('.')[1]) > 2:
            return False
    return s.isdecimal()