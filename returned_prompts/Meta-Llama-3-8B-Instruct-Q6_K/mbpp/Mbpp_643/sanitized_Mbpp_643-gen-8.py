def text_match_wordz_middle(text):
    return 'z' in text[1:-1] and 'z' not in text[0] and 'z' not in text[-1]  # Check if 'z' is in the middle and not at the start or end