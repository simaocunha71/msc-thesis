def text_match_wordz_middle(text):
    for c in text:
        if c == 'z' and (text.startswith('z') or text.endswith('z')):
            return False
    return True