def is_decimal(s: str) -> bool:
    try:
        float(s)
        return s.count('.') == 1 and len(s.split('.')[1]) == 2
    except ValueError:
        return False