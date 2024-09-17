
def is_decimal(s):
    if len(s) != 5:
        return False
    for i in s:
        if not i.isdigit() and i != '.' and i != '0':
            return False
    if s[1] != '.':
        return False
    if s[2] != '0':
        return False
    if s[3] != '0':
        return False
    if s[4] != '0':
        return False
    return True


