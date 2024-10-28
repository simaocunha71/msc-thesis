    if len(strings) == 0:
        return None
    longest_string = strings[0]
    for s in strings:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string


