def text_match_three(txt):
    if txt.startswith('a') and len(txt) >= 3 and txt[1:].startswith('bbb'):
        return True
    return False