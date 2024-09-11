"""
def is_decimal(s):
    if not s.isdigit():
        return False
    else:
        if s.count('.') != 1:
            return False
        else:
            if s.index('.') == 0 or s.index('.') == len(s)-1:
                return False
            else:
                if s.count('0') > 1:
                    return False
                else:
                    if s[0] == '.':
                        return False
                    else:
                        if s[-1] == '.':
                            return False
                        else:
                            return True
"""

"""
from decimal import Decimal

def is_decimal(s):
    try:
        Decimal(s)
        return True
    except ValueError:
        return False
"""

"""
def is_decimal(s):
    if s.count('.') != 1:
        return False
    else:
        if s.index('.') == 0 or s.index('.') == len(s)-1:
            return False
        else:
            if s.count('0') > 1:
                return False
            else:
                return True
"""

"""
def is_decimal(s):
    if s.count('.') != 1:
        return False
    elif s.count('0') > 1:
        return False
    elif s.index('.') == 0 or s.index('.') == len(s)-1:
        return False
    elif s[0] == '.':
        return False
    elif s[-1] == '.':
        return False
    else:
        return True
"""

def is_decimal(s):
    if not s.isdigit():
        return False
    else:
        if s.count('.') != 1:
            return False
        else:
            if s.index('.') == 0 or s.index('.') == len(s)-1:
                return False
            else:
                if s.count('0') > 1:
                    return False
                else: