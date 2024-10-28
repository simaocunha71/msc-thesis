    a = float(a) if ',' in str(a) else int(a)
    b = float(b) if ',' in str(b) else int(b)

    if a == b:
        return None
    elif a > b:
        return a if isinstance(a, float) else str(a)
    else:
        return b if isinstance(b, float) else str(b)

