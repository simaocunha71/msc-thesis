def is_decimal(s):
    try:
        float(s)
        if '.' in s:
            decimal_part = s[s.index('.') + 1:]
            if len(decimal_part) == 2:
                return True
        return False
    except ValueError:
        return False