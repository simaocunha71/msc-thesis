    if not strings:
        return None

    result = strings[0]
    max_length = len(strings[0])

    for s in strings:
        if len(s) > max_length:
            result = s
            max_length = len(s)

    return result

