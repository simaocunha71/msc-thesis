def text_match_wordz_middle(text):
    if text[0]=='z' or text[-1]=='z':
        return False
    if 'z' in text:
        return True
    return False


