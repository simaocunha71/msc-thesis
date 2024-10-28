def reverse_words(s: str) -> str:
    """
    Reverse words in a given string.
    >>> reverse_words("python program")
    'program python'
    """
    words = s.split()
    return ' '.join(words[::-1])