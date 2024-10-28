def find_char_long(my_string, char_length=4):
    return [word for word in my_string.split() if len(word) >= char_length]