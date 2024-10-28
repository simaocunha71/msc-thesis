def count_char_position(s):
    """
    Returns the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
    """
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - ord('a') == i:
            count += 1
    return count