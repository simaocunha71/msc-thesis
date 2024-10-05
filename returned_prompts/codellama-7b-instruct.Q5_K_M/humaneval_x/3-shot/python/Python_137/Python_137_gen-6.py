    if isinstance(a, str):
        a = float(a.replace(',', '.'))

    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    if a == b:
        return None

    if a > b:
        return a

    return b


