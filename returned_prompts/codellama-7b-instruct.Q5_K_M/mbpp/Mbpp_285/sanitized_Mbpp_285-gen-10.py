def text_match_two_three(text):
    if 'a' not in text:
        return False
    index = text.index('a')
    if len(text) - index < 2:
        return False
    if text[index+1] == 'b':
        if len(text) - index < 3:
            return False
        if text[index+2] == 'b':
            return True
        else:
            return False
    else:
        return False