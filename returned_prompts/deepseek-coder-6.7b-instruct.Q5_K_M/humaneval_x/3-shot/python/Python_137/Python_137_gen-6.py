    try:
        if type(a) is str:
            a = float(a.replace(",", "."))
        if type(b) is str:
            b = float(b.replace(",", "."))

        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    except ValueError:
        return None


