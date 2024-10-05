    if a == b:
        return None

    if type(a) == str:
        a = float(a.replace(',', '.'))

    if type(b) == str:
        b = float(b.replace(',', '.'))

    return a if a > b else b

