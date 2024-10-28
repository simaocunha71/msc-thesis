    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    elif isinstance(a, float) and isinstance(b, float):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    elif isinstance(a, str) and isinstance(b, str):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    elif isinstance(a, int) and isinstance(b, float):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    elif isinstance(a, float) and isinstance(b, int):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    elif isinstance(a, str) and isinstance(b, float):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    elif isinstance(a, float) and isinstance(b, str):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    else:
        return None


