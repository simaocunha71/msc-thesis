def text_match_two_three(text):
    if len(text)<3:
        return False
    if text[0] == 'a' and text[1] == 'b' and text[2] == 'b':
        return True
    if text[0] == 'a' and text[1] == 'b' and text[2] == 'b' and text[3] == 'b':
        return True
    return False