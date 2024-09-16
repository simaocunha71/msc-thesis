def text_match_wordz_middle(text):
    if text.startswith('z') and text.endswith('z'):
        return 'z' in text[1:-1]
    else:
        return False
