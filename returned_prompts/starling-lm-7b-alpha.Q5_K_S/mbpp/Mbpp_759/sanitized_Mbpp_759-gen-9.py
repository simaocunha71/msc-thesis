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