    def compare_one(a, b):
        a = float(a) if isinstance(a, str) else a
        b = float(b) if isinstance(b, str) else b
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    return compare_one


