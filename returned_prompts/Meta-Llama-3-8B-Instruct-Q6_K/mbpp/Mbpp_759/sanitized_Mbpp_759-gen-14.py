def is_decimal(s):
    try:
        float(s)
        return len(s.split('.')[1]) <= 2
    except ValueError:
        return False