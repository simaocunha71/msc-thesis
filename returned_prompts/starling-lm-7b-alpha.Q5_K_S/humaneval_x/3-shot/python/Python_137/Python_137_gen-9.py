    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, int) and isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, float) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, str) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, int) and isinstance(b, str):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, float) and isinstance(b, str):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None

    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        elif a < b:
            return b
        elif a == b:
            return None





def compare_one(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a > b, a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return (a