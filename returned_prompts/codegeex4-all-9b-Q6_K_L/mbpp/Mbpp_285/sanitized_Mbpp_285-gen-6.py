def text_match_two_three(text):
    """
    This function checks whether a string contains the 'a' character followed by two or three 'b' characters.
    """
    return re.search(r'a(b{2,3})', text) is not None