def is_decimal(s):
    try:
        float(s)
        if '.' in s and len(s.split('.')[1]) == 2:
            return True
    except ValueError:
        return False