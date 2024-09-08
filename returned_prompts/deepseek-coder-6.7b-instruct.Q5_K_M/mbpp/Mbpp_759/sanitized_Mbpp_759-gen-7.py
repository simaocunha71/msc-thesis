def is_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        parts = s.split('.')
        if len(parts) > 2:
            return False
        elif len(parts) == 2 and len(parts[1]) != 2:
            return False
        return True