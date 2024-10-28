def is_decimal(s):
    try:
        float(s)
        if len(s.split('.')[-1]) == 2:
            return True
    except ValueError:
        return False