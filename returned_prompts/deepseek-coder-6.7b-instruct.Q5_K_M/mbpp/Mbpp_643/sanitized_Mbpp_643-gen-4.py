def text_match_wordz_middle(text):
    for i in range(1, len(text) - 1):
        if text[i] == 'z':
            return True
    return False