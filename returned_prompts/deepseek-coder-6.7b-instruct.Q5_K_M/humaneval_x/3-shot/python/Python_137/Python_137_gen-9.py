    a = float(a) if isinstance(a, str) else a
    b = float(b) if isinstance(b, str) else b

    a = a.replace(',', '.') if isinstance(a, str) else a
    b = b.replace(',', '.') if isinstance(b, str) else b

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None


