    if a == b:
        return None

    if isinstance(a, str):
        a = float(a.replace(",", "."))

    if isinstance(b, str):
        b = float(b.replace(",", "."))

    return max(a, b)

