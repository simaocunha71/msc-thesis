    def convert(val):
        if isinstance(val, str):
            val = val.replace(',', '.')
            return float(val)
        return val

    a, b = convert(a), convert(b)

    if a == b:
        return None
    elif isinstance(a, str) or isinstance(b, str):
        return a if a > b else b
    else:
        return max(a, b)

