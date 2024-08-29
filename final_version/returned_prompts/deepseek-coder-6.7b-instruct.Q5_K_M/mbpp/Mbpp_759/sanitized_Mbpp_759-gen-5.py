def is_decimal(s):
    try:
        num = float(s)
        if '.' in s:
            decimal_part = s.split('.')[1]
            if len(decimal_part) > 2:
                return False
        return True
    except ValueError:
        return False