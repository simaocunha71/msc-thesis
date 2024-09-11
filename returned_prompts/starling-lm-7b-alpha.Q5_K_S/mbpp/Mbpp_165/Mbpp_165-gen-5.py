def count_char_position(s):
    """
    Returns the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
    """
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - ord('a') == i:
            count += 1
    return count

# Test cases
assert count_char_position("xbcefg") == 2
assert count_char_position("abcdefghijklmnopqrstuvwxyz") == 26
assert count_char_position("XbcDEfgh") == 3
assert count_char_position("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 52

# Extra credit:
# assert count_char_position("") == 0
# assert count_char_position(None) == 0






"""
def count_char_position(s):
    """
    Returns the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
    """
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - ord('a') == i:
            count += 1
    return count

# Test cases
assert count_char_position("xbcefg") == 2
assert count_char_position("abcdefghijklmnopqrstuvwxyz") == 26
assert count_char_position("XbcDEfgh") == 3
assert count_char_position("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 52

# Extra credit:
# assert count_char_position("") == 0
# assert count_char_position(None) == 0

"""
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - ord