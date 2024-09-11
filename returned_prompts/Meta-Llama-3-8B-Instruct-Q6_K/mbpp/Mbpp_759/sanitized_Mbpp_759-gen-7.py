def is_decimal(s):
    return s.replace('.','').isdigit() and len(s.replace('.','')) <= 3