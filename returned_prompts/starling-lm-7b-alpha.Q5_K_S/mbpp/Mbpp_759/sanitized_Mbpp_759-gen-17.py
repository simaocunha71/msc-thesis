def is_decimal(s: str):
    if s.count('.') != 1:
        return False
    if len(s.split('.')[1]) != 2:
        return False
    return True