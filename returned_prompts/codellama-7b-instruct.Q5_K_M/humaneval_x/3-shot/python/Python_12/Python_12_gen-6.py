    longest_str = None

    for s in strings:
        if longest_str is None or len(s) > len(longest_str):
            longest_str = s

    return longest_str


