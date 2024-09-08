def find_char_long(string):
    words = string.split(" ")
    four_char_words = [word for word in words if len(word) >= 4]
    return four_char_words