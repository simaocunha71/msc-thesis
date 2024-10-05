    if not strings:
        return None
    longest = strings[0]
    for string in strings[1:]:
        if len(longest) < len(string):
            longest = string
    return longest


