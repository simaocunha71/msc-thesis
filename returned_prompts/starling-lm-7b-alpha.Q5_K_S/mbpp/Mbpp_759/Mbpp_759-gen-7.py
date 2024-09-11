"""
def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1 and s[-2:] == '.' + '0'

def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1 and s.rfind('.') == s.find('.') and s[-2:] == '.' + '0'
"""

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

# assert is_decimal('123.11')==True



"""
def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1 and s[-2:] == '.' + '0'
"""

def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1 and s.rfind('.') == s.find('.') and s[-2:] == '.' + '0'

# assert is_decimal('123.11')==True


"""
def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1
"""

def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1 and s.rfind('.') == s.find('.')

# assert is_decimal('123.11')==True


"""
def is_decimal(s):
    return s.isdigit() and '.' in s and s.count('.') == 1 and len(s) == 4
"""

def is_decimal(s):
    return s