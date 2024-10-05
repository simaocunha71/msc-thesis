
def compare_one(a, b):
    if a == b:
        return None
    if isinstance(a, float):
        return max(a, b)
    if isinstance(b, float):
        return max(a, b)
    if isinstance(a, str):
        if ',' in a:
            a = a.replace(',', '.')
        else:
            a = float(a)
    if isinstance(b, str):
        if ',' in b:
            b = b.replace(',', '.')
        else:
            b = float(b)
    return max(a, b)
