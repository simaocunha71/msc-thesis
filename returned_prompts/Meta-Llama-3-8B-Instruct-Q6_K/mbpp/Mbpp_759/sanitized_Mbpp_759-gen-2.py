def is_decimal(s):
    if s.count('.') == 1:
        left, right = s.split('.')
        if left.isdigit() and right.isdigit() and len(right) <= 2:
            return True
    return False