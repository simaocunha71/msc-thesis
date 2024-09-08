def text_match_wordz_middle(s: str) -> bool:
    """
    Checks if a string contains 'z', except at the start and end of the word.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string contains 'z' except at the start and end of the word, False otherwise.
    """
    return 'z' in s[1:-1]