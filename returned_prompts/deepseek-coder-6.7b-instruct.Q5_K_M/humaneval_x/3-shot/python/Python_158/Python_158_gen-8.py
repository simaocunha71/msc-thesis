    max_len = 0
    max_word = ""
    for word in words:
        unique_chars_len = len(set(word))
        if unique_chars_len > max_len:
            max_len = unique_chars_len
            max_word = word
        elif unique_chars_len == max_len:
            max_word = min(word, max_word)
    return max_word


