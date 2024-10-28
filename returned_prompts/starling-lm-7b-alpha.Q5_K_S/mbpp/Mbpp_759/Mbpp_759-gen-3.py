
def is_decimal(s: str) -> bool:
    if len(s) != 5:
        return False
    if s[0] == '0':
        return False
    if s[3] != '.':
        return False
    if s[2] not in '0123456789':
        return False
    if s[4] not in '0123456789':
        return False
    return True


