    def compare(a, b):
        if isinstance(a, str):
            a = float(a.replace(",", "."))
        if isinstance(b, str):
            b = float(b.replace(",", "."))

        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None

    return compare(a, b) if type(a) != type(b) else compare(a, int(b)) if isinstance(b, int) else compare(int(a), b) if isinstance(a, int) else None


