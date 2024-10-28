def find_char_long(s):
    s = s.split()
    long_words = [word for word in s if len(word) >= 4]
    return long_words