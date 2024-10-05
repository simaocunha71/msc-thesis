
def compare_one(a, b):
    if a == b:
        return None
    elif isinstance(a, str) and isinstance(b, str):
        if '.' in a and ',' in b:
            a = a.replace(',', '.')
            b = b.replace(',', '.')
        elif ',' in a and '.' in b:
            a = a.replace('.', ',')
            b = b.replace('.', ',')
        return a > b and a or b
    else:
        return a > b and a or b
