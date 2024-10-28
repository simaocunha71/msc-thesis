def text_match_wordz_middle(text):
    return bool(re.search(r'[^\bz\b]', text))