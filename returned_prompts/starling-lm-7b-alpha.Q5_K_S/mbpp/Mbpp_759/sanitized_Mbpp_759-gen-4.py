def is_decimal(s):
    return s.isdigit() and '.' in s and len(s.split('.')[1]) == 2