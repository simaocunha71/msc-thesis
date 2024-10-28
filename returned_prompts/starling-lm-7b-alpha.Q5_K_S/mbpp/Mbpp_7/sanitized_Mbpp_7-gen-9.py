def find_char_long(str):
    char_long = set()
    for word in str.split():
        if len(word) >= 4:
            char_long.add(word)
    return char_long