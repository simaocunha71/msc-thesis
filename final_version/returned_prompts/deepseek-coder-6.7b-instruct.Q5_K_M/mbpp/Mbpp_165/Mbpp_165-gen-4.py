def count_char_position(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return sum(1 for a, b in zip(s.lower(), alphabet) if a == b)


print(count_char_position("xbcefg"))  # Output: 2


