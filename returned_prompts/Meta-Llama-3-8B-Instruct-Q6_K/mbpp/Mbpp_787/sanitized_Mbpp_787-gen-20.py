def text_match_three(text):
    if len(text) >= 4 and text[0] == 'a' and text[1:4] == 'bb':
        return True
    return False