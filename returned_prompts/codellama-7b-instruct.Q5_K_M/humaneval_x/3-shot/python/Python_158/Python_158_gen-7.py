    max_length = 0
    res = ""
    for word in words:
        if len(set(word)) > max_length:
            max_length = len(set(word))
            res = word
    return res


