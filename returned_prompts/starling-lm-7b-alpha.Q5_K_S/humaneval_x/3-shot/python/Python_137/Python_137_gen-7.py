    if isinstance(a, int):
        if isinstance(b, int):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(b, float):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(b, str):
            if a == float(b):
                return None
            elif a > float(b):
                return a
            else:
                return float(b)
    elif isinstance(a, float):
        if isinstance(b, int):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(b, float):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(b, str):
            if a == float(b):
                return None
            elif a > float(b):
                return a
            else:
                return float(b)
    elif isinstance(a, str):
        if "," in a:
            a = a.replace(",", ".")
        if "," in b:
            b = b.replace(",", ".")
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        return None


