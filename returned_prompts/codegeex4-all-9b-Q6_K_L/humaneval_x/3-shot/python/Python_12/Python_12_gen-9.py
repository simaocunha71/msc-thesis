    if not strings:
        return None

    max_length = 0
    longest_string = None

    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s

    return longest_string

