def is_decimal(s):
    try:
        float(s)
        if len(s) > 3 and s[2] == '.':
            return True
    except ValueError:
        return False
    return False