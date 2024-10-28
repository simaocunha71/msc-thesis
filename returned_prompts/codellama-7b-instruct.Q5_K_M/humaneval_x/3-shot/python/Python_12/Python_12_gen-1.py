    longest_string = None
    for s in strings:
        if longest_string is None or len(s) > len(longest_string):
            longest_string = s

    return longest_string


