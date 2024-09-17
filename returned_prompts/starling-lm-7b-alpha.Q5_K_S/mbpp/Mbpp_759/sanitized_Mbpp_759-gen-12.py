def is_decimal(s: str) -> bool:
    if len(s) != 4:
        return False
    if s[0] == '.' or s[-1] == '.':
        return False
    if s[1] not in '0123456789':
        return False
    if s[2] not in '0':
        return False
    return True