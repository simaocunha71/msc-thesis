def text_match_wordz_middle(text: str) -> bool:
    text = text.strip()
    if len(text) < 3:
        return False
    return 'z' in text[1:-1]