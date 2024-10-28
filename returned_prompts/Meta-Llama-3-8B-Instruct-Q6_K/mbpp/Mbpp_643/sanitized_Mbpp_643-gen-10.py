def text_match_wordz_middle(text: str) -> bool:
    if len(text) < 3:
        return False
    if text[0].lower() == 'z' or text[-1].lower() == 'z':
        return False
    return 'z' in text[1:-1].lower()  # Check if 'z' is present in the middle of the string