def find_char_long(s):
    """
    Find all words which are at least 4 characters long in a string.

    Args:
    s (str): A string of words.

    Returns:
    set: A set of words with at least 4 characters.
    """
    return set(word for word in s.split() if len(word) >= 4)