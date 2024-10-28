def text_match_two_three(text):
    if len(text) < 3:
        return False
    if text[0] != 'a' or text[1] != 'b':
        return False
    if text[2] != 'b':
        return False
    return True