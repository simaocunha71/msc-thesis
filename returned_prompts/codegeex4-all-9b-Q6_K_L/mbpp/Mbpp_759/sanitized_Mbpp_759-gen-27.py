def is_decimal(s):
    try:
        float(s)
        if s.count('.') == 1:
            return True
    except ValueError:
        pass
    return False