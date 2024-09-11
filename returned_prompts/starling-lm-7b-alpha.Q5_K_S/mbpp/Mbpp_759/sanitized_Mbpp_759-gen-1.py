def is_decimal(s):
    if len(s) != 4:
        return False
    if not s[0].isdigit() or not s[1].isdigit():
        return False
    if s[2] != '.':
        return False
    if not s[3].isdigit() or s[3] != '0':
        return False
    return True