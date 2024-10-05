    if not strings:
        return None

    max_length = len(max(strings, key=len))
    for s in strings:
        if len(s) == max_length:
            return s

    return None


