def find_char_long(string):
    result = []
    for word in string.split():
        if len(word) >= 4:
            result.append(word)
    return result