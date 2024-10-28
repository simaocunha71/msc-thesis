    def to_float_if_possible(value):
        if isinstance(value, str):
            value = value.replace(",", ".")
            try:
                return float(value)
            except ValueError:
                return value
        else:
            return value

    a = to_float_if_possible(a)
    b = to_float_if_possible(b)

    if a == b:
        return None
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    elif isinstance(a, (int, float)):
        return max(a, b)
    else:
        return max(a, b)


