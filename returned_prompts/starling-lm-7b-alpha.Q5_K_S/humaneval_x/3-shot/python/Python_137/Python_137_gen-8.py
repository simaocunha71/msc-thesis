    def compare_one(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (str)):
            if '.' in b:
                b = float(b)
            else:
                b = int(b)
        elif isinstance(a, str):
            if '.' in a:
                a = float(a)
            else:
                a = int(a)

        if a == b:
            return None

        if isinstance(a, int):
            if isinstance(b, int):
                if a > b:
                    return a
                else:
                    return b
            elif isinstance(b, float):
                if a > b:
                    return a
                else:
                    return b
        elif isinstance(a, float):
            if isinstance(b, int):
                if a > b:
                    return a
                else:
                    return b
            elif isinstance(b, float):
                if a > b:
                    return a
                else:
                    return b

        if isinstance(a, str):
            if '.' in a:
                if a > b:
                    return a
                else:
                    return b
            else:
                if a > b:
                    return a
                else:
                    return b



