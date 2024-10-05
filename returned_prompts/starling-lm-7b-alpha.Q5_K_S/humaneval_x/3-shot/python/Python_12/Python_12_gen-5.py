    if len(strings) == 0:
        return None

    longest = strings[0]
    for elem in strings:
        if len(elem) > len(longest):
            longest = elem

    return longest


