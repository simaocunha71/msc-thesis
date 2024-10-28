    if a == b:
        return None

    if isinstance(a, int) and isinstance(b, float):
        return b
    elif isinstance(b, int) and isinstance(a, float):
        return a
    elif isinstance(a, str) and isinstance(b, str):
        if '.' in a and ',' in b:
            a = a.replace(',', '.')
            b = b.replace(',', '.')
        elif ',' in a and '.' in b:
            a = a.replace('.', ',')
            b = b.replace('.', ',')

    if a < b:
        return b
    else:
        return a


