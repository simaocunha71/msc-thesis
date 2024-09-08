def is_decimal(s):
    try:
        float(s)
        if len(s.split('.')[1]) == 2:
            return True
        else:
            return False
    except ValueError:
        return False