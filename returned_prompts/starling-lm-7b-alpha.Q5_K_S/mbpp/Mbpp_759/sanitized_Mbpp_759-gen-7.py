def is_decimal(s):
    if not s.isdigit():
        return False
    if '.' not in s:
        return False
    if s.count('.') != 1:
        return False
    if s.rfind('.') != s.find('.'):
        return False
    if s[-2:] != '.' + '0':
        return False
    return True