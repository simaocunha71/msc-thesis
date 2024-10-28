    max_length = 0
    max_string = ""
    for word in words:
        if len(set(word)) > max_length:
            max_length = len(set(word))
            max_string = word
    return max_string


