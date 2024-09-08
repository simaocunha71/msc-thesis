def is_decimal(s):
    try:
        float(s)
        parts = s.split('.')
        if len(parts) != 2 or len(parts[1]) != 2:
            return False
        return True
    except ValueError:
        return False