def text_match_wordz(text):
    match = re.search(r'\b\w*z\w*\b', text)
    return bool(match)