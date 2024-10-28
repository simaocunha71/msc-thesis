def is_decimal(s):
    if '.' in s:
        left, right = s.split('.')
        if left.isdigit() and right.isdigit() and len(right) <= 2:
            return True
    else:
        if s.isdigit():
            return True
    return False