def is_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return s.startswith('-') or s.endswith('-') or s.count('.') == 1