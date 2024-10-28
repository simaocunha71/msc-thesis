    max_word = ""
    max_len = 0
    for word in words:
        if len(set(word)) > max_len:
            max_word = word
            max_len = len(set(word))

    return max_word


