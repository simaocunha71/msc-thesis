def find_char_long(s):
    return set(word for word in s.split() if len(word) >= 4)  # your code here