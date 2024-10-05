    max_unique = 0
    result = ""

    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique or (len(unique_chars) == max_unique and word < result):
            max_unique = len(unique_chars)
            result = word

    return result

