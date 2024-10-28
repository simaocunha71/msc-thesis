def text_match_wordz_middle(text):
    if text == 'z':
        return True
    elif text.startswith('z'):
        text = text[1:]
    elif text.endswith('z'):
        text = text[:-1]
    else:
        return False
    return 'z' in text


