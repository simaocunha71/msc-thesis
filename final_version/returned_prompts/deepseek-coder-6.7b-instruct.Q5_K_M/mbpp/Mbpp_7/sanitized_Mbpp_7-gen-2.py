def find_char_long(s):
    words = s.split()
    return [word for word in words if len(word) >= 4]