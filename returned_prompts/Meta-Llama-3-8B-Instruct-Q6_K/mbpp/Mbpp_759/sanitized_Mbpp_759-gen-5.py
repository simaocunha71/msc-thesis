def is_decimal(s):
    s = s.strip()
    if s[0] == '-':
        s = s[1:]
    if '.' not in s:
        return False
    left, right = s.split('.')
    if len(left) > 3 or len(right) > 2:
        return False
    return s.replace('.', '', 1).isdigit() and s.replace('.', '', 1).replace('-', '', 1).isdigit() and len(left) <= 3 and len(right) <= 2