    a, b = float(a.replace(',', '.')), float(b.replace(',', '.'))

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b