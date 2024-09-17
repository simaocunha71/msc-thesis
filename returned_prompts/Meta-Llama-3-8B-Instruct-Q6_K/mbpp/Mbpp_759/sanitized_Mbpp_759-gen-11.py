def is_decimal(s):
    if '.' in s:
        left, right = s.split('.')
        if len(left) > 3 or len(right) > 2:
            return False
    else:
        if len(s) > 3:
            return False
    return True