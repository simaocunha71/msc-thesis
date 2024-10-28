    a = float(a) if isinstance(a, str) else a
    b = float(b.replace(',', '.')) if isinstance(b, str) else b

    if a == b:
        return None
    return max(a, b)


