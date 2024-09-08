def is_decimal(s):
    if "." in s:
        parts = s.split('.')
        if len(parts) != 2:
            return False
        if not parts[0].isdigit() or not parts[1].isdigit():
            return False
        if len(parts[1]) > 2:
            return False
    else:
        if not s.isdigit():
            return False
    return True