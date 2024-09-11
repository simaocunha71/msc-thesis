def text_match_three(text):
    """
    Returns True if the string has an a followed by three 'b', and False otherwise.
    """
    if text.startswith('a'):
        return len(text) > 1 and text[1] == 'b' and text[2] == 'b' and text[3] == 'b'
    else:
        return False