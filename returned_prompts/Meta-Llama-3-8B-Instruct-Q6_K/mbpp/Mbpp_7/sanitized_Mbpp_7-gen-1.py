from collections import Counter
def find_char_long(s):
    words = s.split()
    return set(word for word in words if len(word) >= 4)