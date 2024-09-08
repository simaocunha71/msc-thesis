def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    if text[0] == 'z' or text[-1] == 'z':
        return False
    return 'z' in text[1:-1]