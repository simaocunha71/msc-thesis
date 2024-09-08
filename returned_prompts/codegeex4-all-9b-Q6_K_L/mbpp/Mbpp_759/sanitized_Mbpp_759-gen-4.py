def is_decimal(s: str) -> bool:
    try:
        float(s)
        if '.' in s and len(s.split('.')[1]) == 2:
            return True
        else:
            return False
    except ValueError:
        return False