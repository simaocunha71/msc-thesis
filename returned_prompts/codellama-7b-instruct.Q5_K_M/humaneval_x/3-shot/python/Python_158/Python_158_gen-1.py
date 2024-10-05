    max_unique_chars = 0
    max_word = ""
    for word in words:
        if len(set(word)) > max_unique_chars:
            max_unique_chars = len(set(word))
            max_word = word
    return max_word


