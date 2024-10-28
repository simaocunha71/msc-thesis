    if not strings:
        return None

    longest_string = strings[0]
    longest_length = len(longest_string)

    for s in strings[1:]:
        if len(s) > longest_length:
            longest_string = s
            longest_length = len(longest_string)

    return longest_string


