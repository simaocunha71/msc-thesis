    if a == b:
        return None

    return max(a, b, key=lambda x: float(x))


