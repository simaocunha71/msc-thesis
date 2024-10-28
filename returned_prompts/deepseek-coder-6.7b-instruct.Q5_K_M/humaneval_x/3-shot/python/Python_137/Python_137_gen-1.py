    a = a.replace(",", ".") if isinstance(a, str) else a
    b = b.replace(",", ".") if isinstance(b, str) else b

    if a == b:
        return None
    else:
        return max(a, b, key=float)


