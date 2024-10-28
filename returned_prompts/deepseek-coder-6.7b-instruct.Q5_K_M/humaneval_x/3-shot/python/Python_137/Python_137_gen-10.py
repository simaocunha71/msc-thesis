    if a == b:
        return None
    elif type(a) == type(b):
        if type(a) == str:
            a = float(a.replace(',', '.'))
            b = float(b.replace(',', '.'))
        return max(a, b)
    else:
        if type(a) == str:
            a = float(a.replace(',', '.'))
        elif type(b) == str:
            b = float(b.replace(',', '.'))
        return max(a, b)


