def find_char_long(s):
    return set(word for word in s.split() if len(word) >= 4) - set(['to', 'a', 'an', 'the'])  # exclude common short words