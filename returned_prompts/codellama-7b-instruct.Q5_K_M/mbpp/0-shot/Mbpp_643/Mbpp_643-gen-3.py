def text_match_wordz_middle(text):
    if text.startswith('z') or text.endswith('z'):
        return False
    else:
        return 'z' in text
