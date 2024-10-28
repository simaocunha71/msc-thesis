def text_match_three(string):
    """
    Returns True if the string has an a followed by three b's, and False otherwise.
    """
    if len(string) < 3:
        return False
    if string[0] == 'a' and string[1:4] == 'bbb':
        return True
    else:
        return False