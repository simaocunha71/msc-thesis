"""
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if chr(i+65) == s[i].upper():
            count += 1
    return count

assert count_char_position("xbcefg") == 2
"""

