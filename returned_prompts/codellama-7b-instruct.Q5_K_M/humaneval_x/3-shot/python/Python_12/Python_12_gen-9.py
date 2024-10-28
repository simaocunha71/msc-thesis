    if not strings:
        return None

    longest_str = strings[0]
    longest_len = len(longest_str)

    for string in strings:
        if len(string) > longest_len:
            longest_str = string
            longest_len = len(string)

    return longest_str


