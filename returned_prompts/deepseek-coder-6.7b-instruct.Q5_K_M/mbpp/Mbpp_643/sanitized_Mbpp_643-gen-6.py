def text_match_wordz_middle(text):
    import re
    wordz_list = re.findall(r'\b\w*z\w*\b', text)
    for word in wordz_list:
        if word[0] != 'z' and word[-1] != 'z':
            return True
    return False