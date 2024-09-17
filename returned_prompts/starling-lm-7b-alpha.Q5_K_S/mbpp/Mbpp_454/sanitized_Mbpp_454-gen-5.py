def text_match_wordz(word):
    """
    Match a word containing 'z'
    >>> text_match_wordz("pythonz.")
    True
    >>> text_match_wordz("hello")
    False
    """
    return 'z' in word