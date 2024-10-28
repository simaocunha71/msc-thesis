    if len(strings) == 0:
        return None

    max_length = 0
    result = None

    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            result = s

    return result

