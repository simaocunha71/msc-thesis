    if isinstance(a, str):
        a = float(a.replace(",", "."))
    if isinstance(b, str):
        b = float(b.replace(",", "."))

    if abs(a - b) < 1e-6:
        return None
    elif isinstance(a, int) or isinstance(a, float) and a - int(a) == 0:
        if isinstance(b, int) or isinstance(b, float) and b - int(b) == 0:
            return int(a) > int(b)
        else:
            return a
    elif isinstance(b, int) or isinstance(b, float) and b - int(b) == 0:
        return b
    else:
        return a


