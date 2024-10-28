def text_match_wordz_middle(s):
    for i in range(1, len(s)-1):
        if s[i] == 'z':
            return True
    return False