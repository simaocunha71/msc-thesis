def len_log(list_words):
    max_len = 0
    for word in list_words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len