def text_match_wordz_middle(text):
    import re
    if re.search(r'z[a-z]*z', text) and not re.search(r'^z|z$', text):
        return True
    else:
        return False