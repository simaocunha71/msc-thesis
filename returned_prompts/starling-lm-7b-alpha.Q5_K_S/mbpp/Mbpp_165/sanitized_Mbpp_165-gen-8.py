from collections import Counter
def count_char_position(s):
    """Count the number of characters in a string that occur at the same position in the string as in the English alphabet."""
    return sum(s.lower().count(chr(c)) for c in range(ord('a'), ord('z')+1))