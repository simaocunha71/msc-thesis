def is_decimal(s):
    if '.' not in s:
        return s.isdigit() and len(s) <= 3
    else:
        left, right = s.split('.')
        return left.isdigit() and len(left) <= 3 and right.isdigit() and len(right) <= 2