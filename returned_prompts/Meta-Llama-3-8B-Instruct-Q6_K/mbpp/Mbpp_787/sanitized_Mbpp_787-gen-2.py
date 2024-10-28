def text_match_three(text):
    if len(text) < 4:
        return False
    if text[0] != 'a':
        return False
    if text[1] != 'b' or text[2] != 'b' or text[3] != 'b':
        return False
    return True