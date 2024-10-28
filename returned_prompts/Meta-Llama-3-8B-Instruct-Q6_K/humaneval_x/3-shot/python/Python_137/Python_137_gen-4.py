    def compare(a, b):
        if isinstance(a, str) and isinstance(b, str):
            a = float(a.replace(",", "."))
            b = float(b.replace(",", "."))
        elif isinstance(a, str):
            a = float(a.replace(",", "."))
        elif isinstance(b, str):
            b = float(b.replace(",", "."))

        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None

    return compare(a, b)  # This will return the larger variable. If they are equal, it will return None.  # noqa: E501


