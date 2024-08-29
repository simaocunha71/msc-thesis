def text_match_wordz_middle(text):
    return any('z' in word for word in text.split()[1:-1])