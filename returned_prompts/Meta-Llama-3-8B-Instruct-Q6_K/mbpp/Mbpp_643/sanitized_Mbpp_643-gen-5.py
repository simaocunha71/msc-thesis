def text_match_wordz_middle(text: str) -> bool:
    if len(text) < 3:
        return False
    return 'z' in text[1:-1] and text[0] != 'z' and text[-1] != 'z'