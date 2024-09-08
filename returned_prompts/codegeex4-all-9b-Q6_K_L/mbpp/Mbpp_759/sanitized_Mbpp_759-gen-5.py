def is_decimal(s):
    if isinstance(s, str):
        try:
            float(s)
            parts = s.split('.')
            if len(parts) == 2 and len(parts[1]) == 2:
                return True
        except ValueError:
            pass
    return False