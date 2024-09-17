def is_decimal(s):
    if not s: 
        return False
    if s[0] == '-':
        s = s[1:]
    if not set(s).issubset('0123456789.'):
        return False
    if '.' in s:
        left, right = s.split('.')
        if len(right) > 2:
            return False
    return True