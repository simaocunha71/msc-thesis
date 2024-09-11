def text_match_wordz_middle(s):
    if len(s) < 3:
        return False
    if s[0] == 'z' or s[-1] == 'z':
        return False
    return 'z' in s[1:-1] or 'Z' in s[1:-1]  # added 'Z' for case sensitivity