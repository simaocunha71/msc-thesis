def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    if text[0] == 'z' or text[len(text)-1] == 'z':
        return False
    for i in range(1,len(text)-1):
        if text[i] == 'z':
            return True
    return False