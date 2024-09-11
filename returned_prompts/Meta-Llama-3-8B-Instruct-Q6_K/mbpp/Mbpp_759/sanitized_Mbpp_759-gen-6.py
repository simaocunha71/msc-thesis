def is_decimal(s):
    parts = s.split('.')
    if len(parts) > 2:
        return False
    if len(parts) == 2:
        if len(parts[1]) > 2:
            return False
    if not parts[0].isdigit():
        return False
    if parts[1] and not parts[1].replace('.', '', 1).isdigit():
        return False
    return True