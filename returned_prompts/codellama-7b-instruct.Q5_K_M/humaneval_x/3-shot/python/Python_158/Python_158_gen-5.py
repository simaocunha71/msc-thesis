    unique_chars_count = {}
    max_unique_chars = 0
    result = ""

    for word in words:
        unique_chars_count[word] = len(set(word))

        if unique_chars_count[word] > max_unique_chars:
            max_unique_chars = unique_chars_count[word]
            result = word

    return result


