    if not strings:
        return None

    max_length = 0
    max_string = None

    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            max_string = s

    return max_string

