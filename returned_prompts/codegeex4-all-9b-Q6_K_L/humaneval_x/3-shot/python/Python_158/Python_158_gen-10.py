    max_length = 0
    result = ""

    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_length:
            max_length = len(unique_chars)
            result = word
        elif len(unique_chars) == max_length:
            if word < result:
                result = word

    return result

