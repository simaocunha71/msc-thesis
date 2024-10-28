    if type(a) != type(b):
        raise TypeError

    if a == b:
        return None

    if type(a) == int:
        return max(a, b)

    if type(a) == float:
        return max(a, b)

    if type(a) == str:
        if a.replace(".", "").isdigit() and b.replace(".", "").isdigit():
            return max(float(a), float(b))
        if a.replace(",", "").isdigit() and b.replace(",", "").isdigit():
            return max(float(a.replace(",", ".")), float(b.replace(",", ".")))

        if a.replace(",", "").isdigit():
            return max(float(a.replace(",", ".")), b)

        if b.replace(",", "").isdigit():
            return max(a, float(b.replace(",", ".")))

        return max(a, b)
