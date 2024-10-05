    if type(a) == str:
        a = float(a.replace(',', '.'))

    if type(b) == str:
        b = float(b.replace(',', '.'))

    if a == b:
        return None

    return max(a, b) if a > b else min(a, b)