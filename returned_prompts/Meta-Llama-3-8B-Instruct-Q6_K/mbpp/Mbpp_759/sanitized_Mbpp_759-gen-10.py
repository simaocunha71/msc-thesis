def is_decimal(s):
    return s.replace('.', '', 1).isdigit() and len(s) - s.replace('.', '', 1).count('.') <= 1 and len(s) <= 7