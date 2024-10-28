def text_match_wordz_middle(text):
    if 'z' not in text:
        return False
    if text[0]=='z' or text[-1]=='z':
        return False
    else:
        return True