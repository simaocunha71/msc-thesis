    longest_length = 0
    longest_string = None

    for s in strings:
        if len(s) > longest_length:
            longest_length = len(s)
            longest_string = s

    return longest_string


