def is_decimal(s):
    try:
        float(s)
        if '.' in s:
            parts = s.split('.')
            if len(parts[0]) > 0 and len(parts[1]) == 2:
                return True
        return False
    except ValueError:
        return False