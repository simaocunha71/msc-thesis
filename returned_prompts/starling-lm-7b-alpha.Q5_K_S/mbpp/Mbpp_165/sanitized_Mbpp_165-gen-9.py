def count_char_position(s):
    return sum(ord(c) - ord('a') + 1 == i + 1 for i, c in enumerate(s.lower()))
s = "xbcefg"