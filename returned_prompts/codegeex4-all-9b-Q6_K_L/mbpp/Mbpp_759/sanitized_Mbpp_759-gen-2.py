def is_decimal(s):
    try:
        float(s)
        parts = s.split('.')
        if len(parts) == 2 and len(parts[1]) == 2:
            return True
        else:
            return False
    except ValueError:
        return False