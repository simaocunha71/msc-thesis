"""
def count_char_position(str):
    c = 0
    for i in range(26):
        c += str.lower().count(chr(97 + i))
    return c
"""

