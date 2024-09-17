def text_match_three(text):
    if len(text) < 4:
        return False
    if text[0] != 'a':
        return False
    if text[1:4] != 'bbb':
        return False
    return True