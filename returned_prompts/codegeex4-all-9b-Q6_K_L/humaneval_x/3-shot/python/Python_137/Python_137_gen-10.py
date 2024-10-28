    if type(a) == type(b):
        if a == b:
            return None
        else:
            return max(a, b)
    else:
        a = float(a.replace(',', '.')) if isinstance(a, str) else float(a)
        b = float(b.replace(',', '.')) if isinstance(b, str) else float(b)
        return max(a, b) if a != b else None

