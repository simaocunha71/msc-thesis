def is_decimal(s):
    try:
        float(s)
        if s.count('.') != 1 or s.count('0') > 1 or s.index('.') == 0 or s.index('.') == len(s) - 1:
            return False
        return True
    except ValueError:
        return False