    if a == b:
        return None
    if type(a) == type(b):
        return max(a, b)

    if type(a) == str:
        a = float(a.replace(',', '.'))
    if type(b) == str:
        b = float(b.replace(',', '.'))

    return max(a, b)
