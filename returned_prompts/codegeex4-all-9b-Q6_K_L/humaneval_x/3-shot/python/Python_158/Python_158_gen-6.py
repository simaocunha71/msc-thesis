    unique_chars = 0
    result = ""

    for word in words:
        word_unique_chars = len(set(word))
        if word_unique_chars > unique_chars:
            unique_chars = word_unique_chars
            result = word

    return result

