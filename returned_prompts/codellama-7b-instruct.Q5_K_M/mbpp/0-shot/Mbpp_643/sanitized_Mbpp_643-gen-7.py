def text_match_wordz_middle(text):
    if text[0] == 'z' and text[-1] == 'z':
        for i in range(1, len(text)-1):
            if text[i] == 'z':
                return False
        return True
    else:
        return False