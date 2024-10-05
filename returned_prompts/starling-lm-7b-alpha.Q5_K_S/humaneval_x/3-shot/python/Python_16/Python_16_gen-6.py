    char_set = set()
    for char in string:
        char_set.add(char.lower())
    return len(char_set)


