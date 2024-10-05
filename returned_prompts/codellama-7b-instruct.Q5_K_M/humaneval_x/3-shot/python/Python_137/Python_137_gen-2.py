    if a == b:
        return None

    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))
        return max(a, b)
    elif isinstance(a, int) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, int):
        return max(a, b)

    raise TypeError(f"Cannot compare {a} and {b}")
